# Database

Every business record belongs to an organization directly. Tenant isolation is handled by scoped DRF querysets and validated in service functions for workflow actions.

PostgreSQL is the primary database. SQLite is supported for lightweight local test verification.
