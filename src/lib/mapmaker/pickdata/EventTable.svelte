<script>
  let { events, sampleSize } = $props();

  function getRandom(arr, count) {
    // Make a shallow copy of the array to avoid modifying the original
    const shuffled = arr.slice().sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count).sort((a, b) => new Date(a.date) - new Date(b.date));
  }
</script>

<div style="position: relative;">
  <table class="table table-sm">
    <thead>
      <tr>
        <th scope="col" style="white-space: nowrap;">When & Where</th>
        <th scope="col">Who</th>
        <th scope="col">What</th>
      </tr>
    </thead>
    <tbody>
      {#each events.slice(0, sampleSize) as e}
        <tr>
          <td style="white-space: nowrap;">{e.date}<br/>{e.location}</td>
          <td>{e.actor}</td>
          <td>{e.summary}</td>
        </tr>
      {/each}
    </tbody>
  </table>
  {#if events.length > sampleSize}
    <div class="fade-overlay">
    </div>
    <div class="more-notice">
      <p>... these, and the rest, will show up on your map</p>
    </div>
  {/if}
</div>

<style>
  th {
    background-color: var(--palette-light-background);
  }
  td {
    font-size: 0.75rem;
  }
  .fade-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 300px;
    background: linear-gradient(to top, white 40px, transparent);
    pointer-events: none;
  }
  .more-notice {
    position: absolute;
    bottom: 0;
    right: 0;
    font-style: italic;
    padding-right: 2rem;
    pointer-events: none;
  }
</style>