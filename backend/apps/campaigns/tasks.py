from config.celery import app

from .models import Campaign
from .services import send_campaign


@app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def send_campaign_task(self, campaign_id):
    return send_campaign(campaign=Campaign.objects.get(id=campaign_id)).id
