import { defineNuxtConfig } from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/color-mode'],
  buildModules: ['@pinia/nuxt'],
  colorMode: {
    preference: 'system', // default theme
    dataValue: 'theme', // activate data-theme in <html> tag
    classSuffix: '',
  },
  serverMiddleware: [
    { path: '/api/auth', handler: '~/server/api/auth.ts' },
    { path: '/api/auth/**', handler: '~/server/api/auth.ts' },
    { path: '/api/projects', handler: '~/server/api/projects.ts' },
    { path: '/api/projects/**', handler: '~/server/api/projects.ts' },
  ],
})
