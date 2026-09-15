# PulseCRM

PulseCRM is an original, production-style multi-tenant CRM and business operations platform for small and medium-sized teams. It combines company/contact management, leads, sales pipeline, support requests, tasks, projects, email workflows, campaigns, segmentation, analytics, notifications, attachments, imports/exports, audit logging, and search.

## Stack

- Backend: Python 3.12+, Django 6, Django REST Framework, JWT, Celery, Redis, PostgreSQL
- Frontend: React, TypeScript, Vite, React Router, TanStack Query, Tailwind CSS, Recharts
- Quality: pytest, pytest-django, Ruff, TypeScript strict mode, GitHub Actions
- Infrastructure: Docker Compose with backend, frontend, PostgreSQL, Redis, Celery worker, and Celery Beat

## Architecture

```mermaid
flowchart TD
  React[React Frontend] --> API[Django REST API]
  API --> PG[(PostgreSQL)]
  API --> Redis[(Redis)]
  API --> Worker[Celery Worker]
  API --> Beat[Celery Beat]
  API --> SMTP[SMTP / Email Provider]
  API --> Storage[File Storage]
```

## Database

```mermaid
erDiagram
  User ||--o{ OrganizationMembership : has
  Organization ||--o{ OrganizationMembership : includes
  Organization ||--o{ Company : owns
  Organization ||--o{ Contact : owns
  Organization ||--o{ Lead : owns
  Organization ||--o{ Deal : owns
  Organization ||--o{ Product : owns
  Organization ||--o{ CustomerRequest : owns
  Organization ||--o{ Task : owns
  Organization ||--o{ Project : owns
  Organization ||--o{ Note : owns
  Organization ||--o{ Activity : owns
  Organization ||--o{ EmailMessage : owns
  Organization ||--o{ Campaign : owns
  Organization ||--o{ Segment : owns
  Organization ||--o{ Tag : owns
  Organization ||--o{ Notification : owns
  Organization ||--o{ Attachment : owns
  Organization ||--o{ AuditLog : owns
  Company ||--o{ Contact : has
  Company ||--o{ Deal : has
  Contact ||--o{ Deal : influences
  Project ||--o{ Task : contains
```

## Run Locally

```bash
cp .env.example .env
docker compose up --build
```

Backend API: `http://localhost:8000/api/v1/`  
OpenAPI docs: `http://localhost:8000/api/docs/`  
Frontend: `http://localhost:3000/`

Seed demo data:

```bash
docker compose exec backend python manage.py seed_demo_data
```

Demo login: `owner` / `DemoPass123!`

## API Highlights

- `POST /api/v1/auth/register/`
- `POST /api/v1/auth/login/`
- `GET /api/v1/analytics/dashboard/`
- `POST /api/v1/leads/{id}/convert/`
- `POST /api/v1/deals/{id}/advance/`
- `POST /api/v1/tasks/{id}/complete/`
- `GET /api/v1/search/?q=term`

Tenant isolation is enforced server-side through membership-scoped querysets and workflow permission checks.
