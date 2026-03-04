# PuraSecurus
PuraSecurus is a location-focused web application built with Nuxt 3.
The architecture is designed to balance discoverability, security, and performance for map-based experiences.

## Tech Stack
- **CMS**: TinaCloud
- **Client**: Nuxt 3 / TS
- **Server runtime**: Nitro
- **Map library**: MapLibre GL JS
- **Geodata source**: Kartverket API (GeoNorge)

### Architecture Decisions

#### Framework
We are developing a modern application that processes  Geographic data. The core functionality requires the webpage to communicate with external services, to accurately find  & locate Municipalities. and depends on external API to fetch municipalities. 

The main challenge was managing complex data structure that traditionally require separate, manual maintenance. The goal is to replace this fragmented approach with a unified, secure & SEO friendly, resolves these complexities & ensures high visibility on search engines.

By Implementing Nuxt as the primary framework those complexities can be resolved.

-	By moving API communication to the server level, hides sensitive credentials & handle data securely

-	Nuxt renders content on the server making it instantly readable for search engines, unlike standard apps that load content slowly.

-	Nuxt unifies data management, which removes the need for a separate backend maintenance.

#### CMS
We're developing a modern webapp with Nuxt, which requires flexibility and efficient system for content management. Traditionall backend/CMS, requires often a separate database, which separates code and content. While Headless CMS is often git based. As the main goal is to create an architecture that minimize technical overhead, securing tracebacks (Version controll).

- TinaCloud was choosen as a CMS, to utilize the built-in capabilities for Nuxt's (`Nitro`-engine), which ensures seamless communication between Frontend & Backend.

- TinaCloud is designed to push user content into Github, rather than external database, which reduces cost and enhance the efficiency of content delivery.

- TinaCloud Defines Content Schemas as source code, to produce

- TinaCloud takes adventage of **GRAPQL** for precise & efficent queries, minimizing data transer and improve load time.

The integration of TinaCloud unifies the codebase & content, providing a single source of truth within Git. This eliminates database-related overhead, and provides Scalable content management.

#### Libraries
MapLibre GL JS - is a high-performance library for embedding interactive, GPU-accelerated 3D vector maps in web apps.

#### API
Geodata source - Kartverket API (GeoNorge).


## Application Diagrams
-	[Sequence Diagram](./docs/sequenceDiagram.md)
-	[System Context Diagram](./docs/SystemContextDiagram.md)
-	[User Journey Diagram](./docs/userJourney-flowChartDiagram.md)
-	[Form Submission Diagram](./docs/FormSubmission-stateDiagram.md)


## Repository Structure
	-	[Repository Architecture](./docs/architecture.md)
```