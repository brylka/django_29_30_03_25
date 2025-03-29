from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    print("Moje komentarze")
    return render(request, 'myapp/hello_world.html')
    #return HttpResponse("<style> body {background-color: red; color: white;}</style><h1>Hello World!</h1><hr><p>Moja aplikacja</p>")

def hello_name(request, name):
    return render(request, 'myapp/hello_name.html', {'name': name})
    #return HttpResponse(f"Witaj {name}!")

def add(request, a, b):
    c = a + b
    return render(request, 'myapp/add.html', {'a': a, 'b': b, 'c': c})
    #return HttpResponse(f"{a} + {b} = {c}")

def div(request, a, b):
    context = {'a': a, 'b': b}
    if b != 0:
        context['c'] = a / b
    return render(request, 'myapp/div.html', context)
