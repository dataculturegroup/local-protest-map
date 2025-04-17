<script>
  import RightArrow from './icons/arrow-right.svelte';
  let { step } = $props();
</script>

<nav>
  <ul class="step">
    <li class:active={step == 0}><h2>⓵ Pick Data</h2> <div class="arrow"><RightArrow size=30/><div></li>
    <li class:active={step == 1}><h2>⓶ Visualize</h2> <div class="arrow"><RightArrow size=30/><div></li>
    <li class:active={step == 2}><h2>⓷ Embed</h2></li>
  </ul>
</nav>

<style>
  nav {
    margin-bottom: 2rem;
  }
  h2 {
    display: inline-block;
    font-weight: bold;
    font-size: 1.5rem;
    margin: 0;
    padding: 0 1rem 0 0;
  }
  ul.step {
    list-style: none;
    padding: 0;
    margin: 0;
    li {
      position: relative;
      display: inline-block;
      padding: 0 2rem 0.5rem 0;
      margin: 0 1rem 0 0;
      cursor: pointer;
      &.active {
        border-bottom: 2px solid var(--palette-tertiary);
      }
      .arrow {
        position: absolute;
        right: 0px;
        top: 0rem;
      }
    }
  }
</style>