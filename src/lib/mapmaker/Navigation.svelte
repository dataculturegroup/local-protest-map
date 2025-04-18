<script>
  import { passive } from 'svelte/legacy';
  import RightArrow from './icons/arrow-right.svelte';
  let { step, updateStep, okToProceed } = $props();

  function handleNavClick(evt) {
    const clickedStep = evt.currentTarget.getAttribute('data-step');
    if (clickedStep == step) {
      return;
    }
    if (clickedStep < step) {
      updateStep(clickedStep);
    } else {
      if (okToProceed) {
        updateStep(clickedStep);
      }
    }
    evt.preventDefault();
  }
</script>

<nav>
  <a href="#step0" data-step={0} class:active={step == 0} onclick={handleNavClick}>
    <h2>⓵ Choose Protests</h2>
  </a>
  <div class="arrow"><RightArrow size=30/></div>
  <a href="#step1" data-step={1} class:active={step == 1} class:disabled={!okToProceed} onclick={handleNavClick}>
    <h2>⓶ Visualize</h2>
  </a>
  <div class="arrow"><RightArrow size=30/></div>
  <a href="#step2" data-step={2} class:active={step == 2} class:disabled={!okToProceed} onclick={handleNavClick}>
    <h2>⓷ Embed</h2>
  </a>
</nav>

<style>
  nav {
    margin-bottom: 2rem;
    a {
      color: black;
      display: inline-block;
      padding: 0 0 0.5rem 0;
      margin: 0;
      &.active {
        border-bottom: 4px solid var(--palette-tertiary);
      }
      &.disabled{
        color: #666;
        cursor: pointer;
      }
    }
    div.arrow {
      display: inline-block;
      margin: 0 1rem;
    }
    h2 {
      display: inline-block;
      font-weight: bold;
      font-size: 1.5rem;
      margin: 0;
      padding: 0 1rem 0 0;
    }
  }
</style>