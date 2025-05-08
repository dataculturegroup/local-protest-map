<script>
  import html2canvas from 'html2canvas';
  import MapPreview from '../MapPreview.svelte';
  import { onMount } from 'svelte';
  import { preventDefault } from 'svelte/legacy';
  import { DEFAULT_ZOOM, DEFAULT_RADIUS } from '../util/data';

  let { mapSettings, updateStep, events, baseUrl } = $props();

  let computedHeight = $state(null);

  const data = $derived({
    v: 1, // track a version in case this protocol changes in the future
    s: mapSettings.source || 'ACLED',
    c: [mapSettings.coords[0], mapSettings.coords[1]],
    z: mapSettings.zoom || DEFAULT_ZOOM,
    r: mapSettings.radiusMiles || DEFAULT_RADIUS,
    sd: new Date(mapSettings.startDate).toISOString().split('T')[0],
    ed: new Date(mapSettings.endDate).toISOString().split('T')[0],
    w: mapSettings.width || 600,
    h: mapSettings.height || 400,
    i: mapSettings.markerIcon || 'pin',
    t: mapSettings.includeTitle ? 1 : 0,
    m: mapSettings.baseMap || 'alidade-smooth',
    a: mapSettings.stateId || ''
  });
  const params = $derived.by(() => {
    let p = new URLSearchParams();
    Object.entries(data).forEach(([key, value]) => {
      p.append(key, value);
    });
    return p;
  });
  const url = $derived(`${baseUrl}?${params.toString()}`);
  const iframeCode = $derived(`<iframe title="Protest Mapper" aria-label="Map of ${events.length} local protests" id="local-protest-mapper-embed" src="${url}" width="${mapSettings.width}" height="${computedHeight}" frameborder="0" scrolling="no" data-external="1" style="border: none;"></iframe>`);


  function handleDownload() {
    const mapElement = document.querySelector('#mapWrapper');
    html2canvas(mapElement, {
      useCORS: true,
      scale: 2,
      backgroundColor: "#fff"
    }).then(canvas => {
      const link = document.createElement('a');
      link.href = canvas.toDataURL('image/png');
      link.download = 'protest mapper export.png';
      link.click();
    });
  };
</script>

<div class="row">
  <div class="col-md-4">
    <div class="input-group">
      <p>
        Copy and paste the code snippet above into your website to embed it as an iframe.
      </p>
      <form>
        <div class="form-group">
          <label for="embedCode">Embed Code</label>
          <input id="embedCode" type="text" value={iframeCode} readonly size="40">
          <small class="form-text text-muted">
            You can use this HTML code in WordPress, PowerPoint, or other tools that support interactive embedded IFrames.
          </small>
          <button id="copy" class="btn btn-outline btn-lg btn-filled" onclick={(evt) => {navigator.clipboard.writeText(iframeCode); evt.preventDefault()}}>
            Copy Embed Code
          </button>
        </div>
        <div class="form-group">
          <label for="embedCode">Export Image</label>
          <small class="form-text text-muted">
            You can also download the map as a static .png image file.
          </small>
          <button id="#export" class="btn btn-outline btn-lg btn-filled" onclick={(evt) => {handleDownload(); evt.preventDefault();}}>Download Image</button>
        </div>
        </form>
    </div>
    <div class="controls">
      <button class="btn btn-outline-dark btn-lg" onclick={() => updateStep(1)}>
        Previous
      </button>
    </div>
  </div>

  <div class="col-md-8">
    <div class="breakout-content">
      <MapPreview {mapSettings} {events} {baseUrl} bind:computedHeight />
    </div>
  </div>
</div>

<style>
  label {
    display: block;
  }
  .btn-filled {
    background-color: var(--palette-tertiary);
    margin-top: 0.5rem;
  }
  /* important to apply to map container so that it download as an image correctly */
  .breakout-content {
    width: max-content; /* Takes width based on content */
    max-width: none; /* Override Bootstrap max-width limitations */
  }
</style>