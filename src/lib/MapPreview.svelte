<script>
  import Map from './Map.svelte';
  const { mapSettings, events } = $props();
</script>

<section>
  <p>Here's a preview of your map:</p>
  <Map
    center={[mapSettings.coords[1], mapSettings.coords[0]]}
    zoom={mapSettings.zoom}
    markers={events} 
    width={mapSettings.width}
    height={mapSettings.height}
    source={mapSettings.source}
  />
</section>
