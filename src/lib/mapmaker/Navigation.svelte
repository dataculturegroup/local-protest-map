<script>
  let { step } = $props();
</script>

<nav>
  <ul class="step">
    <li class:active={step == 0}><h2>1. Pick Data</h2></li>
    <li class:active={step == 1}><h2>2. Visualize</h2></li>
    <li class:active={step == 2}><h2>3. Embed</h2></li>
  </ul>
</nav>

<style>
  nav {
    margin-bottom: 2rem;
  }
  h2 {
    font-weight: bold;
    font-size: 1rem;
    margin: 0;
    padding: 0;
  }
  ul.step {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  ul.step li {
    display: inline-block;
    padding: 1rem 2rem;
    margin-right: 4rem;
    border: 1px solid var(--palette-tertiary);;
    border-radius: 0.5rem;
    cursor: pointer;
    &.active {
      background-color: var(--palette-tertiary);
    }
  }
</style>