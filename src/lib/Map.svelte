<script>
import { onMount } from 'svelte';
import L from 'leaflet';
let { center, zoom, markers, width, height } = $props();  // center on coords if they are passed in

let map;
let markerLayer;

const stamenToner = L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a> <a href="https://stamen.com/" target="_blank">&copy; Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
  subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 20
});

function createMap(container) {
  map = L.map(container, {preferCanvas: true, scrollWheelZoom: false, zoomControl: false }).setView(center, zoom);
  stamenToner.addTo(map);
  markerLayer = L.layerGroup().addTo(map);
  addMarkers(markers);
}

function addMarkers(markerData) {
  if (!map || !markerLayer) return;
  markerLayer.clearLayers();
  markerData.forEach(function(point) {
    const marker = L.marker([point.lat, point.lon]);
    marker.bindPopup(`<b>${point.date} in ${point.location}</b>`+
                     `<br /><i>${trimToLength(point.actor, 100)}</i><br />${trimToLength(point.summary, 200)}<br />`);
    markerLayer.addLayer(marker);
  });
}

function trimToLength(str, length) {
  if (!str) {
    return "";
  }
  if (str.length > length) {
    return str.substring(0, length) + '...';
  }
  return str;
}

function mapAction(container) {
  createMap(container); 
}

// make sure that the map content and view is updated when new data is passed in
$effect(() => {
  if (!map || !markerLayer) return;
  map.invalidateSize();
  map.setView(center, zoom);
  markerLayer.clearLayers();
  addMarkers(markers);
});
</script>

<div id="mapWrapper" style="width: {width}px; height: {height}px;">
  <div class="map" use:mapAction></div>
</div>

<style>
.map {
  width: 100%;
  height: 100%;
  border: 1px solid #000;
}
</style>

<!-- we need the leaflet stylesheet to get tiles to show up right -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
  integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
  crossorigin=""/>
