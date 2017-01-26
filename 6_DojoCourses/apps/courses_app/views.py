from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Course, Description

# Create your views here.
def index(request):
    context = { "courses": Course.objects.all() }
    return render(request, 'courses_app/index.html', context)

def add(request):
    request.session['name'] = request.POST['name']
    request.session['description'] = request.POST['description']

    verify=True
    if len(request.POST['name'])<15:
        messages.add_message(request, messages.INFO, 'Name field must be at least 15 characters long!')
        verify=False

    if verify:
        del request.session['name']
        del request.session['description']

        course = Course.objects.create(name=request.POST['name'])
        if request.POST['description']:
            if len(request.POST['description'])>0:
                Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')

def show(request,id):
    print Course.objects.get(id=id)
    context = { "course": Course.objects.get(id=id) }
    return render(request, 'courses_app/destroy.html', context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
