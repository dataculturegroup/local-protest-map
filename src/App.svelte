<script>
  import Header from './lib/Header.svelte'
  import MapMaker from './lib/mapmaker/MapMaker.svelte'
  import Footer from './lib/Footer.svelte'

  let coords = $state([]);
</script>

<Header />

<MapMaker />

<Footer />
