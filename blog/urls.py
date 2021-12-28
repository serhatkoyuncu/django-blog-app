from django.urls import path
from .views import post_create, post_list

app_name = 'blog'
urlpatterns = [
    path("",post_list,name="list"),
    path("create/",post_create,name="create"),
]