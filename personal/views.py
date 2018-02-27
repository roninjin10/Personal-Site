from django.shortcuts import render

def about(request):
  return render(request, 'personal/about.html')


def contact(request):
  return render(request, 'personal/basic.html', {'content': ['Do you have a common interest, a question, or just want to chat?  Shoot an email my way and I\'ll be sure to get back to you as soon as I can','willcory10@gmail.com',]})

def projects(request):
  return render(request, 'personal/projects.html')