<script>
  import { map } from 'leaflet';
  import MapPreview from '../MapPreview.svelte';
  let { mapSettings=$bindable(mapSettings), updateStep, events, baseUrl } = $props();
  let computedHeight = $state(null);

  const onMoveEnd = (coords) => {
    if ((coords.lng == mapSettings.coords[0]) && (coords.lat == mapSettings.coords[1])) return;
    mapSettings.coords = [coords.lng, coords.lat];
  };
</script>

<div class="row">
  <div class="col-md-4">
    
    <p>How do you want your map to look? Use these settings to change the map's appearance, 
      then click Next to get the embed code.</p>

    <form>

      <div class="form-group">
        <label for="mapWidth">Size:</label>
        <input type="text" id="mapWidth" bind:value={mapSettings.width} size="5">
        x
        <input type="text" id="mapHeight" bind:value={mapSettings.height} size="5">
        pixels
      </div>

      <div class="form-group">
        <label for="mapCenter">Center:</label>
        <input type="text" id="mapLat" bind:value={mapSettings.coords[0]} size="10" disabled>
        <input type="text" id="matLng" bind:value={mapSettings.coords[1]} size="10" disabled>
        <small id="mapCenterHelp" class="form-text text-muted">
          Drag the map to re-center it.
        </small>
      </div>

      <div class="form-group">
        <input type="checkbox" bind:checked={mapSettings.includeTitle} id="includeTitle">
        <label for="includeTitle">
          Include title?
        </label>
      </div>
     
      <div class="form-group">
        <label for="zoomLevel">Zoom:</label>
        <select id="zoomLevel" name="zoom" bind:value={mapSettings.zoom}>
          <option value=4>4</option>
          <option value=5>5</option>
          <option value=6>6</option>
          <option value=7>7</option>
          <option value=8>8</option>
          <option value=9>9</option>
          <option value=10>10</option>
          <option value=11>11</option>
          <option value=12>12</option>
          <option value=13>13</option>
          <option value=14>14</option>
          <option value=15>15</option>
        </select>
      </div>
<!--
      <div class="form-group">
        <label for="baseMap">Base Map:</label>
        <select id="baseMap" name="baseMap" bind:value={mapSettings.baseMap}>
          <option value='alidade-smooth'>Standard</option>
          <option value='toner'>Black and White</option>
        </select>
      </div>
-->
      <div class="form-group">
        <label for="markerIcon">Icon:</label>        
        <label>
          <input type="radio" name="markerIcon" value="pin" bind:group={mapSettings.markerIcon}>
          <img src="pin.png" alt="a geographic pin marker">
        </label>
        <label>
          <input type="radio" name="markerIcon" value="circle" bind:group={mapSettings.markerIcon}>
          <img src="circle.png" alt="a simple empty circle">
        </label>
        <label>
          <input type="radio" name="markerIcon" value="dot" bind:group={mapSettings.markerIcon}>
          <img src="dot.png" alt="a simple filled dot">
        </label>
        <label>
          <input type="radio" name="markerIcon" value="fist" bind:group={mapSettings.markerIcon}>
          <img src="fist.png" alt="a closed fist">
        </label>
        <label>
          <input type="radio" name="markerIcon" value="sign" bind:group={mapSettings.markerIcon}>
          <img src="sign.png" alt="a sign with an X written on it">
        </label>
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
  <div class="col-md-8">
    <MapPreview {mapSettings} {events} {baseUrl} bind:computedHeight {onMoveEnd} />
  </div>
</div>

<style>
  input[type="text"] {
    text-align: center;
    margin: 0 0.25em;
  }

  /** tweaks to let me use icons for radio buttons **/
  input[type=radio] { 
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
  }
  input[type=radio] + img {
    cursor: pointer;
    width: 50px;
    height: 50px;
    padding: 10px;
  }
  input[type=radio]:checked + img {
    background: var(--palette-tertiary);
    border-radius: 5px;
  }
</style>