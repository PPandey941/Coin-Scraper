from django.db import models
import uuid

class ScrapeJob(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, default='PENDING')
    result = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.job_id)
