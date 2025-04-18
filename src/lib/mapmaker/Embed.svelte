<script>
  let { mapSettings, updateStep, events, baseUrl } = $props();
  import MapPreview from '../MapPreview.svelte';
  import { onMount } from 'svelte';
  import { preventDefault } from 'svelte/legacy';

  const data = $derived({
    v: 1, // track a version in case this protocol changes in the future
    s: mapSettings.source || 'ACLED',
    c: [mapSettings.coords[0], mapSettings.coords[1]],
    z: mapSettings.zoom || 8,
    r: mapSettings.radiusMiles || 50,
    sd: new Date(mapSettings.startDate).toISOString().split('T')[0],
    ed: new Date(mapSettings.endDate).toISOString().split('T')[0],
    w: mapSettings.width || 600,
    h: mapSettings.height || 400,
    i: mapSettings.markerIcon || 'pin',
    t: mapSettings.includeTitle ? 1 : 0
  });
  const params = $derived.by(() => {
    let p = new URLSearchParams();
    Object.entries(data).forEach(([key, value]) => {
      p.append(key, value);
    });
    return p;
  });
  const url = $derived(`${baseUrl}?${params.toString()}`);
  const iframeCode = $derived(`<iframe title="Protest Map" aria-label="Map of ${events.length} local protests" id="local-protest-map-embed" src="${url}" width="${mapSettings.width}" height="${mapSettings.height}" frameborder="0" scrolling="no" data-external="1" style="border: none;"></iframe>`);
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
          <br />
          <input id="embedCode" type="text" value={iframeCode} readonly size="30">
          <br />
          <button id="copy" class="btn btn-outline btn-lg" onclick={(evt) => {navigator.clipboard.writeText(url); evt.preventDefault()}}>
            Copy
          </button>
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
    <MapPreview {mapSettings} {events} {baseUrl} />
  </div>
</div>

<style>
#copy {
  background-color: var(--palette-tertiary);
  margin-top: 0.5rem;
}
</style>