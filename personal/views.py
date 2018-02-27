from django.shortcuts import render
  
def about(request):
  return render(request, 'personal/about.html')


def contact(request):
  return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, please email me','willcory10@gmail.com',]})

def projects(request):
  return render(request, 'personal/projects.html')