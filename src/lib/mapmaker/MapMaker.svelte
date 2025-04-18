<script>
  import { onMount } from 'svelte';
  import dayjs from 'dayjs';

  import Navigation from './Navigation.svelte';
  import PickData from './pickdata/PickData.svelte';
  import Visualize from './Visualize.svelte';
  import Embed from './Embed.svelte';

  let {mapSettings=$bindable(mapSettings), events} = $props();
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
      <PickData bind:mapSettings {updateStep} {events} />
    {:else if step == 1}
      <Visualize bind:mapSettings {updateStep} {events} />
    {:else if step == 2}
      <Embed {mapSettings} {updateStep} {events} />
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