from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hello World!")
