from main_app import views
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', views.index, name='main'),
]
