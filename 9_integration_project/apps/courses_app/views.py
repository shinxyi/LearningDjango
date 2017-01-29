from django.shortcuts import render, redirect
from django.contrib import messages
from ..loginreg_app.models import User
from .models import Course, Description
from django.core.urlresolvers import reverse

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
    return redirect(reverse('courses:index'))

def show(request,id):
    print Course.objects.get(id=id)
    context = { "course": Course.objects.get(id=id) }
    return render(request, 'courses_app/destroy.html', context)

def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect(reverse('courses:index'))

def users_courses(request):
    context = {
        "students_courses": Course.objects.all(),
        "students": User.userManager.all()
     }
    return render(request, 'courses_app/users_courses.html', context)

def add_student(request):
    course = Course.objects.get(id=request.POST['course'])
    student = User.userManager.get(id=request.POST['student'])
    course.students.add(student)
    course.save()
    return redirect(reverse('courses:users_courses'))
