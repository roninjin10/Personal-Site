from django.shortcuts import render
from blog.models import Post

def blog_post(request, title):
  b = Blog(title=title.replace('-',' '))
  return render(request, 'blog/blog_post.html', {'content': b})