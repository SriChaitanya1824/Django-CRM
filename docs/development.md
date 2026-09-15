# Development

Use Docker Compose for the full stack:

```bash
cp .env.example .env
docker compose up --build
```

Run backend tests with:

```bash
DB_ENGINE=django.db.backends.sqlite3 POSTGRES_DB=/tmp/pulsecrm-test.sqlite3 PYTHONPATH=backend pytest -q
```
