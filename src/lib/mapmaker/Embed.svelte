<script>
  let { mapSettings, updateStep, events } = $props();
  import MapPreview from '../MapPreview.svelte';
  import { onMount } from 'svelte';
  import { preventDefault } from 'svelte/legacy';

  const data = $derived({
    s: mapSettings.source,
    c: [mapSettings.coords[0], mapSettings.coords[1]],
    z: mapSettings.zoom,
    r: mapSettings.radiusMiles,
    sd: new Date(mapSettings.startDate).toISOString().split('T')[0],
    ed: new Date(mapSettings.endDate).toISOString().split('T')[0],
    w: mapSettings.width,
    h: mapSettings.height
  });
  const params = $derived.by(() => {
    let p = new URLSearchParams();
    Object.entries(data).forEach(([key, value]) => {
      p.append(key, value);
    });
    return p;
  });
  const url = $derived(`https://dataculture.northeastern.edu/protest-map/?${params.toString()}`);
  const iframeCode = $derived(`<iframe src="${url}" width="${mapSettings.width}" height="${mapSettings.height}" frameborder="0" scrolling="no"></iframe>`);
</script>

<div class="row">
  <div class="col-4">
    <div class="input-group">
      <form class="form-inline">
        <div class="form-group">
          <label for="embedCode">Embed Code</label>
          <input id="embedCode" type="text" class="form-control" value={iframeCode} readonly style="max-width: 100ch;">
          <button class="btn btn-outline-secondary" onclick={(evt) => {navigator.clipboard.writeText(url); evt.preventDefault()}}>
            Copy
          </button>
          <small>
            Copy and paste the code snippet above into your website to embed it as an iframe.
          </small>
        </div>
      </form>
    </div>
    <div class="controls">
      <button class="btn btn-outline-dark btn-lg" onclick={() => updateStep(1)}>
        Previous
      </button>
    </div>
  </div>

  <div class="col-8">
    <MapPreview {mapSettings} {events} />
  </div>
</div>
