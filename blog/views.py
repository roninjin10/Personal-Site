from django.shortcuts import render
from blog.models import Post


def blog_post(request, title):
    b = Post.objects.filter(title=' '.join(title.split('-')))[0]
    return render(request, 'blog/blog_post.html', {'content': [b]})
