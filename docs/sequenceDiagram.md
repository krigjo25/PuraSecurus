````mermaid
---
title: Data Processing Sequence
---
sequenceDiagram
    participant User
    participant NUXT as NUXT Client
    participant SERVER as Nitro Server (API)

    participant ADMIN as Administrator
    participant CMS as Content Management System

    activate User
    activate NUXT
    User ->> NUXT: Submits a Schema for a resturant

    activate SERVER

    Note over SERVER: Server validates the Schema data & ADD API-KEY
    NUXT ->> SERVER: POST /api/v1/restaurants with Schema data

    activate CMS
    SERVER ->> CMS: Generates a Markdown file for the restaurant
    CMS ->> SERVER: Confirms Markdown creation (Git Commit)
    SERVER ->> NUXT: Responds with success message
    deactivate CMS
    deactivate SERVER

    NUXT ->> User: Displays success message
    deactivate NUXT
    activate CMS
    activate ADMIN

    ADMIN ->> CMS: Logs into the CMS to review feedback
    CMS ->> ADMIN: Displays feedback details
    ADMIN ->> CMS: Removes inappropriate content
    CMS ->> ADMIN: Confirms content removal (Git Commit)
    deactivate ADMIN
    deactivate CMS
```