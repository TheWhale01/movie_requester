import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
		host: process.env.VITE_HOST,
		port: Number(process.env.VITE_PORT),
		cors: true,
  },
  preview: {
		port: Number(process.env.VITE_PORT),	
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
