<script>
  import Map from '../Map.svelte';
  let { mapSettings=$bindable(mapSettings), updateStep, events } = $props();

</script>

<div class="container">
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

      </form>

      <div class="controls">
        <button class="btn btn-outline-dark btn-lg" onclick={() => updateStep(0)}>
          Previous
        </button>
        <button class="btn btn-outline-dark primary btn-lg" onclick={() => updateStep(1)}>
          Next
        </button>
      </div>

    </div>
    <div class="col-8">
      <Map
        center={[mapSettings.coords[1], mapSettings.coords[0]]}
        zoom={9}
        markers={events} 
        width={mapSettings.width}
        height={mapSettings.height}
        source={mapSettings.source}
      />
    </div>
  </div>
</div>
