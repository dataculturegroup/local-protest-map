<script>
  import { onMount } from 'svelte';
  import dayjs from 'dayjs';

  import Navigation from './Navigation.svelte';
  import PickData from './pickdata/PickData.svelte';
  import Visualize from './Visualize.svelte';
  import Embed from './Embed.svelte';

  let {mapSettings=$bindable(mapSettings), events, baseUrl} = $props();
  let step = $state(0);

  let okToProceed = $derived.by(() => {
    return (mapSettings.coords.length > 0) && (events.length > 0) && (mapSettings.startDate < mapSettings.endDate);
  });

  function updateStep(newStep) { step = newStep; }
</script>

<main>
  <div class="container">

    <div class="row">
      <div class="col-12">
        <Navigation {step} {updateStep} {okToProceed} />
      </div>
    </div>

    {#if step == 0}
      <PickData bind:mapSettings {updateStep} {events} {okToProceed}/>
    {:else if step == 1}
      <Visualize bind:mapSettings {updateStep} {events} {baseUrl} />
    {:else if step == 2}
      <Embed {mapSettings} {updateStep} {events} {baseUrl} />
    {/if}

  </div>
</main>

<style>
  main {
    background-color: #fff;
  }

  main {
    padding: 4rem 0;
  }
</style>