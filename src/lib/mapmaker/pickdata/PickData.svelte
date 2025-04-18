<script>
  import Locator from "./Locator.svelte";
  import DateInput from './DateInput.svelte';
  import EventTable from './EventTable.svelte';
  import { map } from "leaflet";

  const PREVIEW_SAMPLE_SIZE = 10;

  let { mapSettings=$bindable(mapSettings), updateStep, events, okToProceed } = $props();

</script>

<div class="row">
  <div class="col-md-4">
    <p>What data do you want to map? Use the settings below to configure what protests you want to show up
      on the map. Click next to see a preview and configure how it looks.
    </p>
    <form>

      <div class="form-group">
        <label for="dataSource">Map Area:</label>
        <Locator bind:mapSettings />
        <small id="dataSourceHelp" class="form-text text-muted">
          {#if mapSettings.coords.length > 0}
            You picked: {mapSettings.coords[0].toFixed(4)}, {mapSettings.coords[1].toFixed(4)}
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
      </div>

      <div class="form-group">
        <label>Dates:</label>
        <div id="dateStateEnd" aria-describedby="dateStartEndHelp">
          from <DateInput bind:date={mapSettings.startDate} />
          to <DateInput bind:date={mapSettings.endDate} />
        </div>
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
      {#if okToProceed}
        {#if events.length == 0}
          <p>⚠️ No protests found in this area. Try expanding your radius.</p>
        {:else if events.length > 0}
          <p>Matches <strong>{events.length} protests</strong> in the area. Here's a sample of {PREVIEW_SAMPLE_SIZE} random ones:</p>
          <EventTable {events} sampleSize={PREVIEW_SAMPLE_SIZE}/>
        {/if}
      {:else}
        <p>⚠️ Invalid or missing data - preview not available.</p>
      {/if}
    </section>

  </div>


</div>
