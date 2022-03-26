from django.http import HttpResponse
from django.urls import reverse
from system import urls

def index(request):
    admin = f"""
    <i>Page Working, Please Visit <a href='admin/{urls.secret_url}'>the  Admin Panel!</a> or checkout <a href='{reverse('api:all-jobs')}'>Our API!</a><i>
    """
    return HttpResponse(admin)
