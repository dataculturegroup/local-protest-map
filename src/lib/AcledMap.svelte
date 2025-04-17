<script>
import { onMount } from 'svelte';
import Map from './Map.svelte';
import Papa from 'papaparse';
import isWithinRadius from './geoUtil';
let { coords } = $props();  // center on coords if they are passed in

const radius = 50; // miles
let data = $state(null);  // the full data loaded from CSV on server
let loading = $state(true);
// update the filtered list of local events when the coords or full data change
let localData = $derived(data.filter(
  row => isWithinRadius(coords[1], coords[0], row.latitude, row.longitude, radius)));

const defaultOptions = {
  header: true,               // First row is headers
  dynamicTyping: true,        // Convert numbers/booleans
  skipEmptyLines: true,       // Skip empty rows
  delimitersToGuess: [','], // Try to auto-detect delimiter
};

// fetch CSV data once when map is loaded
onMount(() => {
  fetch("2025-01-01-2025-04-10-North_America-United_States.csv")
    .then(response => response.text())
    .then(csvText => {
      let results = Papa.parse(csvText, defaultOptions);
      data = results.data;
      loading=false;  // to update UI
    });
});
</script>

{#if loading }
  <div class="spinner-border" role="status"></div>
{:else}
  <Map center={[coords[1], coords[0]]} zoom={9} markers={localData} />
{/if}
