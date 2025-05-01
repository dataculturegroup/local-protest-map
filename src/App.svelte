<script>
  import dayjs from 'dayjs';
  import { onMount } from 'svelte'

  import Map from './lib/Map.svelte';
  import Header from './lib/Header.svelte';
  import MapMaker from './lib/mapmaker/MapMaker.svelte';
  import Footer from './lib/Footer.svelte';
  import { getData, isWithinRadius, ACLED_URL, CCC_URL, LAST_UPDATED, randomizeColocatedEvents } from './lib/util/data.js';
  import { marker } from 'leaflet';
  import { userDateStrToDate, userDateStrForDisplay } from './lib/util/date.js';

  const VERSION = '1.3.0';

  const baseUrl = `${document.location.origin}${document.location.pathname}`;

  let urlMapSettings = $state(null);
  let loadingData = $state(true);
  let computedHeight = $state(null); // throwaway placeholder used when rendering embed
  let mapSettings = $state({  // use reasonable defaults
    source: 'ACLED',
    zoom: '8',
    coords: [],
    radiusMiles: '50',
    startDate: '2025-01-01', // hack to get GMT date
    endDate: dayjs(LAST_UPDATED['ACLED']).format('YYYY-MM-DD'), // latest date new data was pulled
    width: 700,
    height: 350,
    markerIcon: 'pin',
    includeTitle: true,
    baseMap: 'alidade-smooth'
  })
  const title = $derived.by(() => { // duplivative, but need it here for embed
    if (mapSettings.includeTitle === false) return null;
    let t = "Protests ";
    t += `between ${userDateStrForDisplay(mapSettings.startDate)} and ${userDateStrForDisplay(mapSettings.endDate)}`;
    return t;
  });
  let data = $state({acled: [], ccc: []});   // filled in by onMount

  let events = $derived.by(() =>{
    let allEvents = [];
    if (mapSettings.source == 'ACLED') {
      allEvents = data.acled;
    } else if (mapSettings.source == 'CCC') {
      allEvents = data.ccc;
    }
    allEvents = allEvents.filter(
      row => isWithinRadius(mapSettings.coords[1], mapSettings.coords[0], row.lat, row.lon, mapSettings.radiusMiles)
    );
    allEvents = allEvents.filter(
      row => {
        const rowDate = new Date(row.date);
        const startDate = userDateStrToDate(mapSettings.startDate);
        const endDate = userDateStrToDate(mapSettings.endDate);
        return (rowDate >= startDate) && (rowDate <= endDate);
      }
    );
    return allEvents;
  });

  onMount( async() => {
    // parse URL params if in embed mode
    const params = new URLSearchParams(window.location.search);
    const urlParams = Object.fromEntries(params.entries());
    try {
      urlMapSettings = {
        source: urlParams.s,
        zoom: urlParams.z,
        coords: urlParams.c.split(',').map(Number),
        radiusMiles: urlParams.r,
        startDate: urlParams.sd,
        endDate: urlParams.ed,
        width: urlParams.w,
        height: urlParams.h,
        markerIcon: urlParams.i,
        includeTitle: urlParams.t == '1',
        baseMap: urlParams.m
      };
    } catch (error) { // bad data on URL, so ignore it
      urlMapSettings = null;
    }
    if (urlMapSettings) {
      mapSettings = urlMapSettings;
    }

    // load and normalize data from various sources
    data.acled = await getData(ACLED_URL);
    data.acled = data.acled.map(row => ({
      lat: row.latitude, lon: row.longitude, date: row.event_date,
      location: `${row.location}, ${row.admin1}`, actor: row.assoc_actor_1,
      summary: row.notes, locRandomized: false
    }));
    data.acled = randomizeColocatedEvents(data.acled);
    data.ccc = await getData(CCC_URL);
    data.ccc = data.ccc.map(row => ({
      lat: row.lat, lon: row.lon, date: row.date,
      location: `${row.resolved_locality}, ${row.resolved_state}`, actor: row.organizations,
      summary: `${row.event_type} ${row.claims_summary}. About ${row.issues}.`, locRandomized: false
    }));
    data.ccc = randomizeColocatedEvents(data.ccc);
    loadingData = false;
  });

</script>

{#if loadingData }

  <div class="spinner-wrapper">
    <div class="spinner-border" role="status"></div>
  </div>

{:else}

  {#if urlMapSettings != null}
    <Map
      title={mapSettings.includeTitle ? title : null}
      zoom={mapSettings.zoom}
      center={[mapSettings.coords[1], mapSettings.coords[0]]}
      markers={events} 
      width={mapSettings.width}
      height={mapSettings.height}
      source={mapSettings.source}
      iconName={mapSettings.markerIcon}
      {baseUrl}
      bind:computedHeight
      baseMap={mapSettings.baseMap}
    />
  {:else}
    <Header />
    <MapMaker bind:mapSettings {events} {baseUrl}/>
    <Footer version={VERSION} />
  {/if}

{/if}

<style>
  .spinner-wrapper {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
</style>