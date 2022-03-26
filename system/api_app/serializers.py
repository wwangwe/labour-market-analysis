from main_app import models
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Job
        fields = '__all__'
