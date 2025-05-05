<script>
  import usStates from './states.json';
  import StateOptions from './StateOptions.svelte';

  import { DEFAULT_ZOOM } from "../../util/data";

  let { mapSettings=$bindable(mapSettings) } = $props();
  let geolocationSupported = navigator.geolocation ? true : false;

  let locating = $state(false);
  let located = $state(false);

  // event handler: use the browser's geolocation API to find the user's location when user clicks "automatically detect" 
  function handleAutoLocate() {
    locating = true;
    navigator.geolocation.getCurrentPosition(handleLocateSuccess, handleLocateError);
  }

  function handleLocateSuccess(position) {
    mapSettings.coords = [position.coords.longitude, position.coords.latitude]; // lon, lat
    locating = false;
    located = true;
    mapSettings.stateId = null; // clear out the stateId
    mapSettings.zoom = DEFAULT_ZOOM; // reset the zoom level
  }

  // event handler: when the browser's geolocation API fails to find the user's location show a reasonable error msg
  function handleLocateError(error) {
    let errorMsg = '';
    switch(error.code) {
        case "unsupported":
            errorMsg = "Browser doesn't support Geolocation.";
            break;
        case error.PERMISSION_DENIED:
            errorMsg = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            errorMsg = "location information is unavailable.";
            break;
        case error.TIMEOUT:
            errorMsg = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            errorMsg = "An unknown error occurred.";
            break;
    }
    alert(errorMsg);
    locating = false;
  }

  $effect( () => {
    let selectedState = usStates.find(row => mapSettings.stateId == row.id);
    if (selectedState) {
      mapSettings.coords = [selectedState.location[1], selectedState.location[0]]; // lat, lon
      mapSettings.zoom = selectedState.zoomLevel;
    }
  });

  function handleStateSelected() {
    if((mapSettings.stateId == null) || (mapSettings.stateId.length == 0)) {
      mapSettings.coords = [];
    } else {
      located = false;
    }
  }
</script>

{#if locating}
  <div class="spinner-wrapper">
    <div class="spinner-border" role="status"></div>
  </div>

{:else}
  <br />
  Within 
  <select id="radius" name="radius" bind:value={mapSettings.radiusMiles}>
    <option value=5>5 miles</option>
    <option value=10>10 miles</option>
    <option value=20>20 miles</option>
    <option value=50>50 miles</option>
    <option value=75>75 miles</option>
    <option value=100>100 miles</option>
  </select>
  of 
  <button id="locateMe" class="btn btn-outline-dark" disabled={!geolocationSupported || located} onclick={handleAutoLocate}>
    {#if located}
      Located position
    {:else}
      Locate Me Now
      {#if !geolocationSupported}
          (not supported)
      {/if}
    {/if}
  </button>

  <div class="text-secondary">
    ( or pick a state
    <select id="stateChoices" onchange={handleStateSelected} bind:value={mapSettings.stateId} aria-describedby="stateChoicesHelp" >
      <option value="">None</option>
      <StateOptions />
    </select> )
  </div>

{/if}

<style>
  .text-secondary select {
    opacity: 0.7;
    margin-top: 0.5rem;
  }
</style>