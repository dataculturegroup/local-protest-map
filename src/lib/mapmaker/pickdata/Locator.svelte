<script>
  import stateLocations from './stateLatLng.json';
  import StateOptions from './StateOptions.svelte';
  let { mapSettings=$bindable(mapSettings) } = $props();
  let geolocationSupported = navigator.geolocation ? true : false;

  let locating = $state(false);
  let located = $state(false);
  let selectedState = $state("");

  // event handler: use the browser's geolocation API to find the user's location when user clicks "automatically detect" 
  function handleAutoLocate() {
    locating = true;
    navigator.geolocation.getCurrentPosition(handleLocateSuccess, handleLocateError);
  }

  function handleLocateSuccess(position) {
    mapSettings.coords = [position.coords.longitude, position.coords.latitude]; // lon, lat
    locating = false;
    located = true;
    selectedState = ""; // reset the state selection
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

  function handleStateSelected() {
    const latlon = stateLocations[selectedState];
    if (latlon.length == 0) { 
      mapSettings.coords = [];  // reset to nothing
      return; 
    }
    mapSettings.coords = [latlon[1], latlon[0]]; // lat, lon
    located = false;
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

  <br />

  <span class="text-secondary">( or pick a state
  <select id="stateChoices" onchange={handleStateSelected} bind:value={selectedState} aria-describedby="stateChoicesHelp" >
    <option value="">None</option>
    <StateOptions />
  </select> )</span>

{/if}

<style>
  .text-secondary select {
    opacity: 0.7;
  }
</style>