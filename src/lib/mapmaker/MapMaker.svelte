<script>
  import { onMount } from 'svelte';
  import { getData, isWithinRadius } from './data.js';
  import dayjs from 'dayjs';

  import Navigation from './Navigation.svelte';
  import PickData from './pickdata/PickData.svelte';
  import Visualize from './Visualize.svelte';
  import Embed from './Embed.svelte';

  const ACLED_URL = "2025-01-01-2025-04-10-North_America-United_States.csv";

  let loadingData = $state(true);
  let mapSettings = $state({
    source: 'ACLED',
    coords: [],
    radiusMiles: '50',
    startDate: dayjs('2025-01-01', 'YYYY-MM-DD').toDate(), // hack to get GMT date
    endDate: new Date(), // default to today
    width: 800,
    height: 400
  })
  let data = $state({
    acled: [],
  })
  let events = $derived.by(() => {
    if (mapSettings.source == 'ACLED') {
      return data.acled.filter(
        row => isWithinRadius(mapSettings.coords[1], mapSettings.coords[0], row.latitude, row.longitude, mapSettings.radius)
      );
    }
  });

  let step = $state(0);

  function updateStep(newStep) { step = newStep; }

  onMount( async ()=> {
    data.acled = await getData(ACLED_URL);
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
        <Embed bind:mapSettings />
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