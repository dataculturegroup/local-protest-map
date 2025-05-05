<script>
  import states from './states.json';
</script>

{#each states as usState}
    <option value={usState['id']}>{usState['name']}</option>
{/each}
