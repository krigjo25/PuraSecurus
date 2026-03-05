# PuraSecurus
PuraSecurus is a location-focused web application built with Python. The architecture is
designed to balance discoverability, security, & performance for map-based experiences.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Git
- (Optional) Redis for session management and caching

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/krigjo25/PuraSecurus.git
   cd PuraSecurus
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   See [requirements.txt](./requirements.txt) for the complete list of dependencies.

### Running the Application

1. **Start the development server**
   ```bash
   reflex run
   ```

2. **Access the application**
   - Frontend: `http://localhost:3000`
   - API documentation: `http://localhost:8000/docs`

### Key Dependencies
- **FastAPI** - Backend API framework
- **Reflex** - Python-based frontend framework
- **Pydantic** - Data validation and schema definition
- **PyDeck** - Map visualization with GPU acceleration
- **Pandas/GeoPandas** - Geospatial data processing
- **SQLAlchemy/SQLModel** - Database ORM

## Architectural Decisions

### Architecture Question
How do we keep one simple and consistent user experience across content pages, forms, and maps,
while also meeting security needs and keeping page load times fast?

### Techstack
-	Backend Technology: **FastAPI**
-	Backend/Frontend: **Python (Reflex + HTMX)**
-	Data Validation: **Pydantic** (Sikrer dataintegritet fra eksterne API-er)
-	Data Engine: **Pandas / GeoPandas**
-	Native CMS: Wagtail (Headless) eller FastAPI-Markdown (Innholdsstyring direkte i Python)

-	Map Library: **Pydeck** (basert på deck.gl)
-	Geodata source: **Kartverket API** (GeoNorge)


### Architectural Justification
#### Unified Language Strategy (Python)
Python was chosen for both backend and frontend-related logic to keep development simple and
consistent.

**Same language everywhere**
Using one language means less confusion, faster teamwork, and easier onboarding for new
developers.

**One shared data model**
The same municipality and geodata models can be used across the app, which reduces errors and
keeps behavior predictable.

**Less glue code**
When everything is in Python, we avoid extra conversion layers between different languages.
That saves time and reduces bugs.

#### FastAPI as Backend Core
FastAPI is used because it is fast, clear, and easy to maintain. For PuraSecurus, this gives:
- A clear API boundary for map and municipality endpoints
- Stable validation and error handling for external geodata
- Built-in API documentation and easier testing

### Data Integerty with Pydantic
Since PuraSecurus relies on critical geographic data from `Kartverket API`, Pydantic is used
as a strict validation layer before data reaches the UI.

**Why this matters**
- Invalid or incomplete data is stopped early
- Clean, consistent schemas make map rendering stable
- Shared models reduce crashes and unexpected UI behavior

This turns uncertain external data into trusted internal data that can be used safely across
the app.

### Integrated Content Management (CMS)
The architecture handles complex maps while keeping the site fast and secure. Heavy map data
processing runs on the server, where credentials and integration keys stay protected.

All text and images are versioned in GitHub, which gives:
- Full traceability for content and configuration changes
- Simple rollback when regressions are detected
- A lightweight editorial workflow without a dedicated content database in early phases

This gives a practical path: start simple now, then move to a headless CMS later if content
needs become larger.

### Performance and Security Posture
- **Server-side geoprocessing (Pandas/GeoPandas):** keeps heavy computation off user devices
	and gives more consistent results across browsers.
- **Thin client map rendering (Pydeck):** keeps the browser focused on drawing the map quickly.
- **Controlled data exposure:** only required fields are returned to clients, reducing attack
	surface and payload size.
- **Strong validation + typed routes:** makes issues easier to trace and fix.

### Repository Structure
	-	[Repository Architecture](./docs/architecture.md)

## Application Diagrams
-	[Sequence Diagram](./docs/sequenceDiagram.md)
-	[System Context Diagram](./docs/SystemContextDiagram.md)
-	[User Journey Diagram](./docs/userJourney-flowChartDiagram.md)
-	[Form Submission Diagram](./docs/FormSubmission-stateDiagram.md)