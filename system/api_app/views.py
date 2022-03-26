from main_app import models
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_app import serializers


@api_view(['GET'])
def all_jobs(request):
    jobs = models.Job.objects.all()
    jobs_serializer = serializers.JobSerializer(jobs, many=True)
    return Response(jobs_serializer.data)
