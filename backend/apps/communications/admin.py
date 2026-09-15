from django.contrib import admin

from .models import EmailAccount, EmailMessage, EmailSignature, EmailTemplate

admin.site.register(EmailAccount)
admin.site.register(EmailMessage)
admin.site.register(EmailTemplate)
admin.site.register(EmailSignature)
