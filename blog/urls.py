from django.urls import path
from django.views.generic import ListView
from blog.models import Post
from . import views

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by('-date'), template_name='blog/blog.html')),
    path('<str:title>/', views.blog_post),
]
