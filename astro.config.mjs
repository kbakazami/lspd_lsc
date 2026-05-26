import { defineConfig } from 'astro/config';
import sanity from '@sanity/astro';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';
import vercel from '@astrojs/vercel';

export default defineConfig({
  adapter: vercel(),
  image: {
    domains: ['cdn.sanity.io'],
  },
  integrations: [
    sanity({
      projectId: 'ybq4sq6q',
      dataset: 'production',
      apiVersion: '2026-05-20',
      useCdn: true,
      studioBasePath: '/studio',
    }),
    react(),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});