<script>
  import Locator from "./Locator.svelte";
  import DateInput from './DateInput.svelte'
  
  let { mapSettings=$bindable(mapSettings), updateStep, events } = $props();

  let dataValid = $derived(() => {
    return (mapSettings.coords.length > 0);
  });

</script>

<div class="row">
  <div class="col-md-6">
    <form class="form-inline">

      <div class="form-group">
        <label for="dataSource">Data Source</label>
        
        <select class="form-control" id="dataSource" aria-describedby="dataSourceHelp" bind:value={mapSettings.source}>
          <option value="ACLED">ACLED (Armed Conflict Location & Event Data</option>
        </select>

        <small id="dataSourceHelp" class="form-text text-muted">Which data about protests do you want to map?</small>
      </div>

      <div class="form-group">
        <label for="dataSource">Area</label>
        Within 
        <select class="form-control" id="radius" name="radius" bind:value={mapSettings.radiusMiles}>
          <option value=20>20 miles</option>
          <option value=50>50 miles</option>
          <option value=75>75 miles</option>
          <option value=100>100 miles</option>
        </select>
         of 
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

    {#if dataValid()}
      {#if events.length == 0}
        <div class="alert alert-warning" role="alert">
          No protests found in this area. Try expanding your radius.
        </div>
      {:else if events.length > 0}
        <div class="alert alert-success" role="alert">
          Matches {events.length} protests in the area.
        </div>
      {/if}
    {/if}

    <div class="controls">
      <button class="btn btn-outline-dark primary btn-lg" onclick={() => updateStep(1)} disabled={!dataValid()}>
        Next
      </button>
    </div>
    
  </div>
</div>
