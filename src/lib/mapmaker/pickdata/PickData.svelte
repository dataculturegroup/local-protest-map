<script>
  import Locator from "./Locator.svelte";
  import EventTable from './EventTable.svelte';
  import { map } from "leaflet";
  import { userDateStrForDisplay, dateStrForDisplay } from "../../util/date";
  import { CANVAS_MAP_THRESHOLD } from "../../util/data";
  import { LAST_UPDATED } from "../../util/data";

  const PREVIEW_SAMPLE_SIZE = 20;

  let { mapSettings=$bindable(mapSettings), updateStep, events, okToProceed } = $props();

  const userPickedLocation = $derived((mapSettings.coords.length > 0) || ((mapSettings.stateId != null) && (mapSettings.stateId.length > 0)));
  
  const endDateTooRecent = $derived(new Date(mapSettings.endDate) > LAST_UPDATED[mapSettings.source]);

  $effect(() => {
    if (events.length > CANVAS_MAP_THRESHOLD) {
      mapSettings.markerIcon = 'dot';
    } else {
      mapSettings.markerIcon = 'pin';
    }
  })
</script>

<div class="row">
  <div class="col-md-4">
    <p>What data do you want to map? Use the settings below to configure what protests you want to show up
      on the map. Click next to see a preview and configure how it looks.
    </p>
    <form>

      <div class="form-group">
        <label for="radius">Map Area:</label>
        <Locator bind:mapSettings />
        <small id="radiusHelp" class="form-text text-muted">
          {#if mapSettings.coords.length > 0}
            Map will be centered 
            {#if mapSettings.stateId}
              on {mapSettings.stateId}
            {:else}
              at: {mapSettings.coords[0].toFixed(4)}, {mapSettings.coords[1].toFixed(4)}
            {/if}
          {:else}
            ⚠️ Pick a location
          {/if}
        </small>
      </div>

      <div class="form-group">
        <label for="dataSource">Data Source:</label>        
        <select id="dataSource" aria-describedby="dataSourceHelp" bind:value={mapSettings.source}>
          <option value="ACLED">ACLED</option>
          <option value="CCC">CCC</option>
        </select>
        <small id="dataSourceHelp" class="form-text text-muted">
          {mapSettings.source} includes data through {dateStrForDisplay(LAST_UPDATED[mapSettings.source])}.
        </small>
      </div>

      <div class="form-group">
        <label for="startDate">Dates:</label>
        <div id="dateStateEnd" aria-describedby="dateStartEndHelp">
          from <input type="date" id="startDate" name="startDate" bind:value={mapSettings.startDate} />
            to <input type="date" id="endDate" name="endDate" bind:value={mapSettings.endDate} />
        </div>
        {#if endDateTooRecent }
          <small id="dateStartEndHelp" class="form-text text-danger">
            ⚠️ The end date is too recent. {mapSettings.source} only includes data through {dateStrForDisplay(LAST_UPDATED[mapSettings.source])}.
          </small>
        {/if}
      </div>

    </form>

    <div class="controls">
      <button class="btn btn-outline-dark primary btn-lg" onclick={() => updateStep(1)} disabled={!okToProceed}>
        Next
      </button>
    </div>
    
  </div>

  <div class="col-md-8">
    <section style="min-height: 500px;">
      {#if userPickedLocation}
        {#if events.length == 0}
          <p>⚠️ No protests found in this area. Try expanding your radius.</p>
        {:else if events.length > 0}
          <p>Found <strong>{events.length} protests</strong> 
            from {mapSettings.source} data in 
            {mapSettings.stateId ? mapSettings.stateId : "the area"} 
            between {userDateStrForDisplay(mapSettings.startDate)} and {userDateStrForDisplay(mapSettings.endDate)}.
            Here are the most recent:</p>
          <EventTable {events} sampleSize={PREVIEW_SAMPLE_SIZE} />
        {/if}
      {:else}
        <div id="preview">
          <img src="table-preview.png" width="100% " alt="Preview of the table" />
          <p>Pick a location, then you'll see a list of matching protests here.</p>
        </div>
      {/if}
    </section>

  </div>

</div>

<style>
  #preview {
    font-style: italic;
  }

  #preview {
    position: relative;
    img {
      filter: blur(3px);
      opacity: 0.5;
    }
    p {
      position: absolute;
      top: 1rem;
      left: 1rem;
      background-color: white;
      padding: 0.5rem 1rem;
    }
  }
</style>