"""system URL Configuration"""
from decouple import config
from django.contrib import admin
from django.urls import path, include

secret_url = config('SECRET_ADMIN_URL')

urlpatterns = [
    path('admin/' + secret_url, admin.site.urls),
    path('', include('main_app.urls')),
    path('api/', include('api_app.urls')),
]
