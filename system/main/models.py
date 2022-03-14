from django.db import models


class Job(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=75, blank=False)
    location = models.CharField(max_length=20, blank=False)
    function = models.CharField(max_length=50, blank=False)
    industry = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)
    qualifications = models.TextField(max_length=20000, blank=False)
    link = models.CharField(max_length=75, blank=False)