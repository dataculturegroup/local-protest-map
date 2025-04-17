<script>
  import AcledMap from './lib/AcledMap.svelte'
  import Locator from './lib/Locator.svelte'
  import Share from './lib/Share.svelte'

  let coords = $state([]);

</script>

<main>
  <div class="row">
    <div class="col-lg-6">
      <h1>Where are Protests Happening?</h1>
      <p>
        Protests are popping up regularly in towns and cities all over the US in response to Trump administration actions, but understanding the timeline and scale is important context for local stories. You can create an embeddable map of local protests that you can add to your stories to help readers see local actions.
      </p>
      <Locator bind:coords />
    </div>
    <div class="col-lg-6">
      {#if (coords.length==2)}
        <AcledMap {coords} />
      {/if}
    </div>
  </div>

  <Share />
  
</main>

<style>

</style>
