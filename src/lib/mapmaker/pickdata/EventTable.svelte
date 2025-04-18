<script>
  let { events, sampleSize } = $props();

  function getRandom(arr, count) {
    // Make a shallow copy of the array to avoid modifying the original
    const shuffled = arr.slice().sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count).sort((a, b) => new Date(a.date) - new Date(b.date));
  }
</script>

<table class="table table-sm">
  <thead>
    <tr>
      <th scope="col" style="white-space: nowrap;">When & Where</th>
      <th scope="col">Who</th>
      <th scope="col">What</th>
    </tr>
  </thead>
  <tbody>
    {#each getRandom(events, sampleSize) as e}
      <tr>
        <td style="white-space: nowrap;">{e.date}<br/>{e.location}</td>
        <td>{e.actor}</td>
        <td>{e.summary}</td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  th {
    background-color: var(--palette-light-background);
  }
  td {
    font-size: 0.75rem;
  }
</style>