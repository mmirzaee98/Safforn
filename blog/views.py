from django.shortcuts import render
from blog.models import Blog

def blog(request, pk):
    page = Blog.objects.get(pk=pk, publish=True)
    return render(request, 'blog.html', {'blog': page})

def blogs(request):
    objects = Blog.objects.filter(publish=True)
    return render(request, 'blogs.html',{'blogs':objects})
