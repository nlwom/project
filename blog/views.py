from django.shortcuts import render ,redirect
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', { 'blogs': blogs })

def deta(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'deta.html', { 'blog': blog })

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.writer = request.GET['writer']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))


def update(request, id):
    blog = Blog.objects.get(id = id)
    blog.title = request.GET['title']
    blog.writer = request.GET['writer']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return render('/blog/' + str(blog.id))
    