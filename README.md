# PuraSecurus
PuraSecurus is a location-focused web application built with Nuxt 3.
The architecture is designed to balance discoverability, security, and performance for map-based experiences.

## Architecture Decisions
Nuxt 3 is chosen over a client-only Vue setup to solve key platform requirements:

- **SEO & discoverability**: Server-side rendering (SSR) helps search engines index restaurant pages and municipality listings correctly.
- **Secure geodata handling**: Nitro server routes handle reverse geocoding and data lookups on the server, keeping API keys out of the browser.
- **Hybrid performance**: SSR delivers fast initial content, while `<ClientOnly>` is used for heavier interactive map components.
- **CMS-friendly content model**: The project can use a CMS-driven workflow for location content without requiring a traditional backend-heavy architecture.

## Tech Stack

- **CMS**: TinaCloud
- **Frontend**: Nuxt 3
- **Server runtime**: Nitro
- **Map library**: MapLibre GL JS
- **Geodata source**: Kartverket API (GeoNorge)

## Documentation

- [System Context Diagram](./docs/SystemContextDiagram.md)
- [Sequence Diagram](./docs/sequenceDiagram.md)

## Repository Structure

```text
docs/
	sequenceDiagram.md
	SystemContextDiagram.md
README.md
```