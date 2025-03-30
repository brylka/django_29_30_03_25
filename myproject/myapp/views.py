from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LinearEquationForm, PostForm
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
    sort = request.GET.get('sort', 'id')
    posts = Post.objects.all().order_by(sort)
    return render(request, 'myapp/post_list.html', {'posts': posts})

def create_post(request):
    #if request.method == "POST":
        #title = request.POST.get("title")
        #content = request.POST.get("content")
        #if title and content:
        #    Post.objects.create(title=title, content=content)
        #else:
        #    return HttpResponse("Nie wszystkie dane są podane!")
    #form = PostForm()
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("post_list")
    return render(request, 'myapp/post_form.html', {'form': form, 'title': 'Stwórz post'})

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        #post.title = request.POST.get("title")
        #post.content = request.POST.get("content")
        #post.save()
        form.save()
        return redirect("post_list")

    return render(request, 'myapp/post_form.html', {'form': form, 'title': 'Edytuj post'})

# def delete_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect("post_list")
#
#     return render(request, 'myapp/delete_post.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "DELETE":
        post.delete()
        return JsonResponse({"message": "Post usunięty!"}, status=200)
    return JsonResponse({"error": "Metoda nieznana!"}, status=405)


def zero_point(request):
    if request.method == 'POST':
        form = LinearEquationForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']

            if a != 0:
                x0 = -b / a
            else:
                x0 = 'Brak miejsca zerowyego!'
    else:
        x0 = None
        form = LinearEquationForm()

    return render(request, 'myapp/zero_point.html', {'form': form, 'x0': x0})