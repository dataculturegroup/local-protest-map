<script>
import Geolocation from "svelte-geolocation";
import stateLocations from './stateLatLng.json';
import StateOptions from './StateOptions.svelte';
let { coords=$bindable(coords) } = $props();

let locateMe = $state(false);
let selectedState = $state("");


function handleAutoLocate() {
  locateMe = true;
  const theButton = document.getElementById('locateMe');
  theButton.disabled = true;
}

function handleStateSelected() {
  const loc = stateLocations[selectedState];
  if (value.length == 0) { 
    coords = [];  // reset to nothing
    return; 
  }
  coords = [loc[1], loc[0]]; // lat, long
}
</script>

<button id="locateMe" class="btn btn-outline-dark" onclick={() => handleAutoLocate()}>Locate Me</button>
or pick a state

<select id="stateChoices" class="form-control" onchange={handleStateSelected} bind:value={selectedState} aria-describedby="stateChoicesHelp" >
  <option value="">None</option>
  <StateOptions />
</select>

{#if locateMe}
  <Geolocation getPosition bind:coords />
{/if}

