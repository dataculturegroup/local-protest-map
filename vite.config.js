import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  base: '/local-protest-map/',
  build: {
    outDir: 'docs',
    emptyOutDir: true,
  }
})
