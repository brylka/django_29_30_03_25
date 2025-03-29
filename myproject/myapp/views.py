from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    print("Moje komentarze")
    return render(request, 'myapp/hello_world.html')
    #return HttpResponse("<style> body {background-color: red; color: white;}</style><h1>Hello World!</h1><hr><p>Moja aplikacja</p>")

def hello_name(request, name):
    return HttpResponse(f"Witaj {name}!")