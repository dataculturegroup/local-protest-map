<script>
  import dayjs from 'dayjs';

  import Navigation from './Navigation.svelte';
  import PickData from './pickdata/PickData.svelte';
  import Visualize from './Visualize.svelte';
  import Embed from './Embed.svelte';

  let mapSettings = $state({
    source: 'ACLED',
    coords: [],
    startDate: dayjs('2025-01-01', 'YYYY-MM-DD').toDate(), // hack to get GMT date
    endDate: new Date(), // default to today
  })
  let step = $state(0);

  function updateStep(newStep) { step = newStep; }
</script>

<main>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <Navigation {step} />
      </div>
    </div>

      {#if step == 0}
        <PickData bind:mapSettings {updateStep} />
      {:else if step == 1}
        <Visualize bind:mapSettings />
      {:else if step == 2}
        <Embed bind:mapSettings />
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