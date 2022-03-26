from django.http import HttpResponse
from system import urls

def index(request):
    admin = f"""
    <i>Page Working, Please Visit <a href='admin/{urls.secret_url}'>the  Admin Panel!</a><i>
    """
    return HttpResponse(admin)
