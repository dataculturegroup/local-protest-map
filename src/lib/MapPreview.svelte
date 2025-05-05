<script>
  import Map from './Map.svelte';
  import { autoTitle } from './util/string.js';
  let { mapSettings, events, baseUrl, computedHeight=$bindable(computedHeight), onMoveEnd=null } = $props();
  
  const title = $derived.by(() => autoTitle(mapSettings));
</script>

<section>
  <p>Here's a preview of your map:</p>
  <Map
    {title}
    center={[mapSettings.coords[1], mapSettings.coords[0]]}
    zoom={mapSettings.zoom}
    markers={events} 
    width={mapSettings.width}
    height={mapSettings.height}
    source={mapSettings.source}
    iconName={mapSettings.markerIcon}
    {baseUrl}
    bind:computedHeight
    {onMoveEnd}
    baseMap={mapSettings.baseMap}
  />
</section>
