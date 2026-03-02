# Overview of PuraSecurus

## Architecture decision

### The Argument
The project using Nuxt 3 as a framework, insted of pure Vue, to solve three critical challanges for location services :

    -   **SEO & Discoverability** - Using Server-sided Rendering (SSR) ensures that resturant pages and Municipality lists indexing correctly through the search engine, which is crucial for user experience.

    -   **Secure Geodata Handling** - By using the built-in server engine (Nitro), we can perform reverse geocoding & database queries on the server-side. This secures API-keys and reduces the load on the client.

    -   **Performance through Hybrid Rendering** - By combining SSR for Static Information & ```<ClientOnly>``` for heavy map components, we optimize "Time to Content" while the geolocation keeps its interactivity.

    -   **Available for CMS** - With SSR framework, we do not need traditional backend or database to solve the issue. We can use a CMS to document new locations.

## Techstack
    CMS : **TinaCloud**
    Client : **Nuxt v3**
    Geo Library : **MapLibre GL JS**
    Geo Data Source : **Kartverket API** ( Geo Norge )

##  Context Diagram
[System Context Diagram](./docs/SystemContextDiagram.md)
[Sequence Diagram](./docs/SequenceDiagram.md)
[State Diagram](./docs/StateDiagram.md)