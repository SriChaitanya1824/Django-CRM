import csv
from io import StringIO

from django.db import transaction

from apps.contacts.models import Contact


@transaction.atomic
def import_contacts(*, organization, csv_text, owner=None):
    reader = csv.DictReader(StringIO(csv_text))
    created, errors = 0, []
    for index, row in enumerate(reader, start=2):
        try:
            Contact.objects.create(organization=organization, first_name=row.get("first_name") or row["email"].split("@")[0], last_name=row.get("last_name", ""), email=row["email"], phone=row.get("phone", ""), owner=owner)
            created += 1
        except Exception as exc:
            errors.append({"row": index, "error": str(exc)})
    return {"created": created, "errors": errors}


def export_contacts(*, organization):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["first_name", "last_name", "email", "phone", "status"])
    for contact in Contact.objects.filter(organization=organization).iterator():
        writer.writerow([contact.first_name, contact.last_name, contact.email, contact.phone, contact.status])
    return output.getvalue()
