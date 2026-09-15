# Deployment

Set `DJANGO_DEBUG=False`, configure `ALLOWED_HOSTS`, use managed PostgreSQL and Redis, and provide SMTP and object-storage credentials through environment variables.

The Dockerfiles are suitable as a base for container platforms. Run migrations before promoting a release.
