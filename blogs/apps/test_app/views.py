from django.shortcuts import render, redirect
from .models import Blog, Comment

def index(request):
    context = {
    "blogs": Blog.objects.all()
    # select * from Blog
    }
    print(Blog.objects.all())
    return render(request, 'test_app/index.html', context)

def blogs(request):
    # using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    # insert into Blog (title, blog, created_at, updated_at) values (title, blog, now(), now())
    return redirect('/')
def comments(request,id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'],blog=blog)
    return redirect('/')
