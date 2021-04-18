from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def registerPage(request):
    return render(request, 'useraccount/login.html')
    # return HttpResponse('Register Hapa')


def index(request):
    return HttpResponse('Home Page')
