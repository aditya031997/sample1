from django.http import HttpResponse
def index (request):
    return HttpResponse("<h1>Hello World</h1>")

def home(request):
    return HttpResponse("<h1>welcome to hello world</h1>")
