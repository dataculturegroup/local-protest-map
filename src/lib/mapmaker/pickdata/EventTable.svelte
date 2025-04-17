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
      <th scope="col">Date</th>
      <th scope="col">Location</th>
      <th scope="col">Actor</th>
      <th scope="col">Summary</th>
    </tr>
  </thead>
  <tbody>
    {#each getRandom(events, sampleSize) as e}
      <tr>
        <td style="white-space: nowrap;">{e.date}</td>
        <td style="white-space: nowrap;">{e.location}</td>
        <td>{e.actor}</td>
        <td>{e.summary}</td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  th {
    background-color: var(--palette-light-background);
    margin-right: 1px;
  }
  td {
    font-size: 0.75rem;
  }
</style>