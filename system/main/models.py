from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=50, blank=False)
    function = models.CharField(max_length=100, blank=False)
    industry = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    qualifications = models.TextField(max_length=50000, blank=False)
    scrap_date = models.DateField(auto_now_add=True)
    hyperlink = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.title
