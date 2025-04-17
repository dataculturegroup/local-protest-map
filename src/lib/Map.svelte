<script>
import { onMount } from 'svelte';
import L from 'leaflet';
let { center, zoom, markers } = $props();  // center on coords if they are passed in

let map;
let markerLayer;

const stamenToner = L.tileLayer('https://tiles.stadiamaps.com/tiles/stamen_toner_lite/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a> <a href="https://stamen.com/" target="_blank">&copy; Stamen Design</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
  subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 20
});

function createMap(container) {
  map = L.map(container, {preferCanvas: true }).setView(center, zoom);
  stamenToner.addTo(map);
  markerLayer = L.layerGroup().addTo(map);
  addMarkers(markers);
}

function addMarkers(markerData) {
  if (!map || !markerLayer) return;
  markerLayer.clearLayers();
  markerData.forEach(function(point) {
    const marker = L.marker([point.latitude, point.longitude]);
    let actors = point.assoc_actor_1 ? point.assoc_actor_1 : '';
    marker.bindPopup(`<b>${point.event_date} in ${point.location}, ${point.admin1}</b>`+
                     `<br /><i>${actors}</i><br />${point.notes}<br />`);
    markerLayer.addLayer(marker);
  });
}

function mapAction(container) {
  createMap(container); 
}

// make sure that the map content and view is updated when new data is passed in
$effect(() => {
  if (!map || !markerLayer) return;
  map.setView(center, zoom);
  markerLayer.clearLayers();
  addMarkers(markers);
});
</script>

<div class="map" use:mapAction></div>

<style>
.map {
  height: 600px;
  width: 600px;
  border: 1px solid #000;
}
</style>

<!-- we need the leaflet stylesheet to get tiles to show up right -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
  integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
  crossorigin=""/>
