<script>
  import { onMount } from 'svelte';
  import { getData, isWithinRadius } from '../util/data.js';
  import dayjs from 'dayjs';

  import Navigation from './Navigation.svelte';
  import PickData from './pickdata/PickData.svelte';
  import Visualize from './Visualize.svelte';
  import Embed from './Embed.svelte';

  const ACLED_URL = "2025-01-01-2025-04-10-North_America-United_States.csv";
  const CCC_URL = "ccc-phase3-public.csv";

  let loadingData = $state(true);
  let mapSettings = $state({
    source: 'ACLED',
    zoom: '8',
    coords: [],
    radiusMiles: '50',
    startDate: dayjs('2025-01-01', 'YYYY-MM-DD').toDate(), // hack to get GMT date
    endDate: new Date(), // default to today
    width: 700,
    height: 350
  })
  let data = $state({acled: [], ccc: []});   // filled in by onMount
  let events = $derived.by(() => {
    let allEvents = [] 
    if (mapSettings.source == 'ACLED') {
      allEvents = data.acled;
    } else if (mapSettings.source == 'CCC') {
      allEvents = data.ccc;
    } 
    return allEvents.filter(
      row => isWithinRadius(mapSettings.coords[1], mapSettings.coords[0], row.lat, row.lon, mapSettings.radiusMiles)
    );
  });

  let step = $state(0);

  function updateStep(newStep) { step = newStep; }

  onMount( async ()=> {
    // load and normalize data from various sources
    data.acled = await getData(ACLED_URL);
    data.acled = data.acled.map(row => ({
      lat: row.latitude, lon: row.longitude, date: row.event_date,
      location: `${row.location}, ${row.admin1}`, actor: row.assoc_actor_1,
      summary: row.notes
    }));
    data.ccc = await getData(CCC_URL);
    data.ccc = data.ccc.map(row => ({
      lat: row.lat, lon: row.lon, date: row.date,
      location: `${row.resolved_locality}, ${row.resolved_state}`, actor: row.organizations,
      summary: `${row.event_type} ${row.claims_summary}. About ${row.issues}.`
    }));
    loadingData = false;
  });

</script>

<main>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <Navigation {step} />
      </div>
    </div>

    {#if loadingData }
    
      <div class="spinner-border" role="status"></div>
    
    {:else}

      {#if step == 0}
        <PickData bind:mapSettings {updateStep} {events} />
      {:else if step == 1}
        <Visualize bind:mapSettings {updateStep} {events} />
      {:else if step == 2}
        <Embed {mapSettings} {events} />
      {/if}
    
    {/if}

  </div>
</main>

<style>
  main {
    background-color: #fff;
  }

  main {
    padding: 2rem 0rem;
  }
</style>