# Architecture

PulseCRM is a modular monolith. Each domain lives in `backend/apps/<domain>` with models, serializers, viewsets, services, admin, migrations, and tests where behavior is important.

The frontend is a Vite React application with a persistent CRM layout, route-level pages, API client, and reusable list/dashboard components.
