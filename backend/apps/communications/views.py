from apps.common.crud import viewset_for

from .models import EmailAccount, EmailMessage, EmailSignature, EmailTemplate
from .serializers import (
    EmailAccountSerializer,
    EmailMessageSerializer,
    EmailSignatureSerializer,
    EmailTemplateSerializer,
)

EmailAccountViewSet = viewset_for(EmailAccount, EmailAccountSerializer, ["name", "email_address"])
EmailMessageViewSet = viewset_for(EmailMessage, EmailMessageSerializer, ["subject", "sender"])
EmailTemplateViewSet = viewset_for(EmailTemplate, EmailTemplateSerializer, ["name", "subject"])
EmailSignatureViewSet = viewset_for(EmailSignature, EmailSignatureSerializer, ["name"])
