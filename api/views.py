from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapeJob
from .tasks import scrape_coin_data
from .serializers import ScrapeJobSerializer
import uuid


class StartScraping(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        if not coins:
            return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)

        job_id = uuid.uuid4()
        job = ScrapeJob.objects.create(job_id=job_id, status='PENDING')

        scrape_coin_data.delay(job_id, coins)

        return Response({'job_id': job_id}, status=status.HTTP_200_OK)


class ScrapingStatus(APIView):
    def get(self, request, job_id):
        try:
            job = ScrapeJob.objects.get(job_id=job_id)
        except ScrapeJob.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ScrapeJobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
