from django.http import HttpResponse
def details(request):
    return HttpResponse("<h3>This Place is for Details<h3>")