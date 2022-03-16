from django.http import HttpResponse


def index(request):
    admin = f"""
    <i>Page Working, Please Visit <a href='/admin'>the  Admin Panel!</a><i>
    """
    return HttpResponse(admin)
