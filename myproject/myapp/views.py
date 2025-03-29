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

def table(request):
    posts = [
        {'title': 'Post pierwszy', 'content': 'Terść pierwszego posta', 'created_at': '2025-03-10'},
        {'title': 'Post drugi  ', 'content': 'Terść drugiego posta', 'created_at': '2025-03-13'},
        {'title': 'Post trzeci  ', 'content': 'Terść trzeciego posta', 'created_at': '2025-03-16'},
        {'title': 'Post czwarty', 'content': 'Terść czwartego posta', 'created_at': '2025-03-20'},
        {'title': 'Post piąty', 'content': 'Terść piątego posta', 'created_at': '2025-03-24'},
    ]

    # text = ''
    # for post in posts:
    #     text += (f"{post['title']}\t\t\t{post['content']}\t\t{post['created_at']}<br>\n")
    return render(request, 'myapp/tables.html', {'posts': posts})
    #return HttpResponse(text)


if __name__ == '__main__':
    table()