# PulseCRM — Project Plan

## Objectives
Build a modular monolith CRM (PulseCRM) with multi-tenancy, role-based access, REST API, React frontend, background processing with Celery, and production-ready tooling (Docker, CI).

## Phase 1 (this sprint)
- Repository inspection
- Project skeleton (backend + frontend)
- Docker & docker-compose
- Django project and core apps (`accounts`, `organizations`)
- JWT authentication scaffold
- Multi-tenancy model and membership
- Base React app with Tailwind and layout
- CI config skeleton

## Folder structure
- backend/ — Django project and apps
- frontend/ — React + Vite + TypeScript
- docs/ — design and runbooks
- .github/ — CI workflows

## Next steps
Follow PHASE 1 tasks and iterate. Each phase will include tests, migrations, demo data, and documentation.
# PulseCRM Project Plan

1. Foundation: Django/DRF, React/Vite, Docker, CI, tenant models, auth.
2. CRM Core: companies, contacts, tags, notes, activities.
3. Leads: lead workflow and conversion service.
4. Sales: deal pipeline and stage validation.
5. Work: requests, tasks, projects, reminders, notifications.
6. Communications: email accounts/messages/templates/signatures, campaigns, segments.
7. Analytics: dashboard aggregations, global search, import/export.
8. Hardening: attachments, audit logs, admin, tests, documentation.

Current implementation provides a production-style vertical slice across all phases with migrations and focused behavioral tests.
