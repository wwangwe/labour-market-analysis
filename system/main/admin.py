from django.contrib import admin

from main import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('scrap_date', 'title', 'location', 'function', 'industry')
    list_filter = ('scrap_date', 'location', 'function', 'industry')