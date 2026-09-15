from apps.common.crud import serializer_for

from .models import EmailAccount, EmailMessage, EmailSignature, EmailTemplate

EmailAccountSerializer = serializer_for(EmailAccount)
EmailMessageSerializer = serializer_for(EmailMessage)
EmailTemplateSerializer = serializer_for(EmailTemplate)
EmailSignatureSerializer = serializer_for(EmailSignature)
