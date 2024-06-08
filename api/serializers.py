from rest_framework import serializers
from .models import ScrapeJob

class ScrapeJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapeJob
        fields = ['job_id', 'status', 'result']
