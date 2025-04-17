<script>
  import MapPreview from '../MapPreview.svelte';
  let { mapSettings=$bindable(mapSettings), updateStep, events } = $props();

</script>

<div class="row">
  <div class="col-4">
    
    <form class="form-inline">

      <div class="form-group">
        <label for="mapWidth">Size</label>
        <div class="input-group mb-2 mr-sm-2">
          <input type="text" class="form-control" id="mapWidth" bind:value={mapSettings.width}>
          <div class="input-group-append">
            <div class="input-group-text">px</div>
          </div>
        </div>
        x
        <div class="input-group mb-2 mr-sm-2">
          <input type="text" class="form-control" id="mapHeight" bind:value={mapSettings.height}>
          <div class="input-group-append">
            <div class="input-group-text">px</div>
          </div>
        </div>
      </div>

      <div class="form-group">
        <label for="zoomLevel">Zoom</label>
        <select class="form-control" id="zoomLevel" name="zoom" bind:value={mapSettings.zoom}>
          <option value=5>5</option>
          <option value=6>6</option>
          <option value=7>7</option>
          <option value=8>8</option>
          <option value=9>9</option>
          <option value=10>10</option>
        </select>

      </div>

    </form>

    <div class="controls">
      <button class="btn btn-outline-dark btn-lg" onclick={() => updateStep(0)}>
        Previous
      </button>
      <button class="btn btn-outline-dark primary btn-lg" onclick={() => updateStep(2)}>
        Next
      </button>
    </div>

  </div>
  <div class="col-8">
    <MapPreview {mapSettings} {events} />
  </div>
</div>
