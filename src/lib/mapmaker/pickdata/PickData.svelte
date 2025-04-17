<script>
  import Locator from "./Locator.svelte";
  import DateInput from './DateInput.svelte'
  
  let { mapSettings=$bindable(mapSettings), updateStep } = $props();

  let dataValid = $derived(() => {
    return (mapSettings.coords.length > 0);
  });

</script>

<div class="row">
  <div class="col-md-6">
    <form>

      <div class="form-group">
        <label for="dataSource">Data Source</label>
        
        <select class="form-control" id="dataSource" aria-describedby="dataSourceHelp">
          <option value="ACLED">ACLED (Armed Conflict Location & Event Data</option>
        </select>

        <small id="dataSourceHelp" class="form-text text-muted">Which data about protests do you want to map?</small>
      </div>

      <div class="form-group">
        <label for="dataSource">Area</label>

        <Locator bind:coords={mapSettings.coords}/>
        <small id="dataSourceHelp" class="form-text text-muted">Where do you want the map to center?
          {#if mapSettings.coords.length > 0}
            You picked: {mapSettings.coords[0].toFixed(4)}, {mapSettings.coords[1].toFixed(4)}
          {:else}
            ⚠️ Pick a location
          {/if}
        </small>

      </div>

      <div class="form-group">
        <label for="dateStartEnd">Dates</label>

        <div id="dateStateEnd" aria-describedby="dateStartEndHelp">
          from <DateInput bind:date={mapSettings.startDate} />
          to <DateInput bind:date={mapSettings.endDate} />
        </div>

        <small id="dateStartEndHelp" class="form-text text-muted">What dates do you want to include?</small>
      </div>

    </form>

    <div class="controls">
      <button class="btn btn-outline-dark primary" onclick={() => updateStep(1)} disabled={!dataValid()}>
        Next
      </button>
    </div>
    
  </div>
</div>

<style>
label {
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}
.form-group {
  margin-bottom: 1rem;
}
small {
  display: block;
}
</style>