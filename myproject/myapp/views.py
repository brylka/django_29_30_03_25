from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post


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


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title and content:
            Post.objects.create(title=title, content=content)
            return redirect("post_list")
        else:
            return HttpResponse("Nie wszystkie dane są podane!")

    return render(request, 'myapp/create_post.html')

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("post_list")

    return render(request, 'myapp/update_post.html', {'post': post})