<script>
    import stateLatLng from './stateLatLng.json';
    const stateNames = Object.keys(stateLatLng);
</script>

{#each stateNames as stateName}
    <option value={stateName}>{stateName}</option>
{/each}
