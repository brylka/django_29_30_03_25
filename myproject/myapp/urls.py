from django.urls import path
from .views import hello_world, hello_name, add, div

urlpatterns = [
    path('hello/', hello_world),
    path('hello/<str:name>/', hello_name),
    path('add/<int:a>/<int:b>/', add),
    path('div/<int:a>/<int:b>/', div),
]