from django.urls import path
from .views import hello_world, hello_name, add, div, table, post_list, create_post, update_post, delete_post, \
    zero_point, image_list, create_image, serve_image

urlpatterns = [
    path('hello/', hello_world, name="hello_world"),
    path('hello/<str:name>/', hello_name),
    path('add/<int:a>/<int:b>/', add),
    path('div/<int:a>/<int:b>/', div),
    path('tables/', table),
    path('posts/', post_list, name="post_list"),
    path('posts/create/', create_post, name="create_post"),
    path('posts/update/<int:post_id>/', update_post, name="update_post"),
    path('posts/delete/<int:post_id>/', delete_post, name="delete_post"),

    path('zero-point/', zero_point, name="zero_point"),

    path('images/', image_list, name="image_list"),
    path('images/create/', create_image, name="create_image"),
    path('images/serve/<int:image_id>/', serve_image, name="serve_image"),
]