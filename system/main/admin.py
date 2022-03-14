from django.contrib import admin

from main import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'location', 'function', 'industry')
    list_filter = ('date', 'location', 'function', 'industry')