<script>
  import Map from './Map.svelte';
  let { mapSettings, events, baseUrl, computedHeight=$bindable(computedHeight), onMoveEnd=null } = $props();
  
  const title = $derived.by(() => {
    if (mapSettings.includeTitle === false) return null;
    let t = "Protests ";
    const formatDate = (date) => new Date(date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    t += `between ${formatDate(mapSettings.startDate)} and ${formatDate(mapSettings.endDate)}`;
    return t;
  });

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
