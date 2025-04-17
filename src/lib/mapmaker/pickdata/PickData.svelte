<script>
  import Locator from "./Locator.svelte";
  import DateInput from './DateInput.svelte';
  import EventTable from './EventTable.svelte';

  const PREVIEW_SAMPLE_SIZE = 10;

  let { mapSettings=$bindable(mapSettings), updateStep, events } = $props();

  let dataValid = $derived(() => {
    return (mapSettings.coords.length > 0);
  });

</script>

<div class="row">
  <div class="col-md-4">
    <form class="form-inline">

      <div class="form-group">
        <label for="dataSource">Data Source</label>
        
        <select class="form-control" id="dataSource" aria-describedby="dataSourceHelp" bind:value={mapSettings.source}>
          <option value="ACLED">ACLED (Armed Conflict Location & Event Data</option>
          <option value="CCC">CCC (Crowd Counting Consortium @ Harvard Kennedy School)</option>
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

    <div class="controls">
      <button class="btn btn-outline-dark primary btn-lg" onclick={() => updateStep(1)} disabled={!dataValid()}>
        Next
      </button>
    </div>
    
  </div>

  <div class="col-md-8">
    <section>

      {#if dataValid()}
        {#if events.length == 0}
          <p>No protests found in this area. Try expanding your radius.</p>
        {:else if events.length > 0}
          <p>Matches <strong>{events.length} protests</strong> in the area. Here's a sample of {PREVIEW_SAMPLE_SIZE} random ones:</p>
          <EventTable {events} sampleSize={PREVIEW_SAMPLE_SIZE}/>
        {/if}
      {:else}
        <p>Preview not available until you pick a location.</p>
      {/if}
    </section>

  </div>


</div>
