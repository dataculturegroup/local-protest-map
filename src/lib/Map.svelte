<script>
import { onMount } from 'svelte';
import { trimToLength } from './util/string';
import L from 'leaflet';
let { source, center, zoom, markers, width, height, title, baseUrl, iconName, 
  computedHeight=$bindable(computedHeight), onMoveEnd=null } = $props();  // center on coords if they are passed in

let map;
let markerLayer;

const stamenToner = L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png', {
  attribution: '',
  subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 20
});

function createMap(container) {
  map = L.map(container, {preferCanvas: true, scrollWheelZoom: false, zoomControl: false }).setView(center, zoom);
  stamenToner.addTo(map);
  markerLayer = L.layerGroup().addTo(map);
  addMarkers(markers);
  if (onMoveEnd) {
    map.on('moveend', () => onMoveEnd(map.getCenter()));
  }
}

function addMarkers(markerData) {
  if (!map || !markerLayer) return;
  const icon = L.icon({
    iconUrl: `${iconName}.png`,
    iconSize:     [30, 30], // size of the icon
    iconAnchor:   [15, 30], // point of the icon which will correspond to marker's location
    popupAnchor:  [0, -30] // point from which the popup should open relative to the iconAnchor
  });
  markerLayer.clearLayers();
  markerData.forEach(function(point) {
    const marker = L.marker([point.lat, point.lon],  {icon});
    marker.bindPopup(`<b>${point.date} in ${point.location}</b>`+
                     `<br /><i>${trimToLength(point.actor, 100)}</i><br />${trimToLength(point.summary, 200)}<br />`);
    markerLayer.addLayer(marker);
  });
}

function mapAction(container) {
  createMap(container); 
}

onMount(() => {
  const mapWrapper = document.getElementById('mapWrapper');
  if (mapWrapper) {
    computedHeight = mapWrapper.offsetHeight;
  }
})

// make sure that the map content and view is updated when new data is passed in
$effect(() => {
  if (!map || !markerLayer) return;
  map.setView(center, zoom);
  markerLayer.clearLayers();
  addMarkers(markers);
  const mapWrapper = document.getElementById('mapWrapper');
  if (mapWrapper) {
    computedHeight = mapWrapper.offsetHeight;
  }
  map.invalidateSize({debounceMoveend: true});
});
</script>

<figure id="mapWrapper">
  {#if title}
    <h3>{title}</h3>
  {/if}
  <div class="map" use:mapAction style="width: {width}px; height: {height}px;"></div>
  <figcaption  style="width: {width}px;">
    Created with <a href={baseUrl}>Protest Map</a>. Data via
    {#if source == "ACLED"}
      <a href="https://www.acleddata.com" target=_new>Armed Conflict Location & Event Data Project (ACLED)</a>
    {:else if source == "CCC"}
      <a href="https://ash.harvard.edu/programs/crowd-counting-consortium/" target=_new>Crowd Counting Consortium - Ash Center - Harvard Kennedy School.</a>
    {/if}.
    <br />
    Map tiles &copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a> <a href="https://stamen.com/" target="_blank">&copy; Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>
  </figcaption>
</figure>

<style>
h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}
.map {
  width: 100%;
  height: 100%;
  border: 1px solid #999;
  overflow: hidden;
  position: relative;
}
figcaption {
  display: block;
  color: #fff;
  padding: 5px;
  font-size: 0.7rem;
  background-color: #999;
  a {
    color: #fff;
    &:hover {
      color: #fff;
    }
    &:active {
      color: #fff;
    }
    &:visited {
      color: #eee;
    }
  }
}
</style>

<!-- we need the leaflet stylesheet to get tiles to show up right -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
  integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
  crossorigin=""/>
