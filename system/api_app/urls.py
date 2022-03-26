from django.urls import path

from api_app import views

app_name = 'api'
urlpatterns = [
    path('all-jobs/', views.all_jobs, name='all-jobs'),
]
