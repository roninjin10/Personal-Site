from django.shortcuts import render
from blog.models import Post

def blog_post(request, title):
  try:
    b = Post.objects.filter(title= title.replace('-',' '))
  except Post.DoesNotExist:
    raise Http404("Post does not exist")
  return render(request, 'blog/blog_post.html', {'content': [b]})