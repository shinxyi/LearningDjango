from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'loginreg_app/index.html')
def register(request):
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    request.session['birthday'] = request.POST['birthday']
    if len(User.userManager.filter(email=request.POST['email']))>0:
        messages.add_message(request, messages.ERROR, 'Please check your email...')
        return redirect('/')
    user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['birthday'], request.POST['password'], request.POST['confirm_password'])
    if 'errors' in user:
        for err in user['errors']:
            messages.add_message(request, messages.ERROR, err)
        return redirect('/')
    user = user['user']
    user = User.userManager.create(first_name= user['first_name'], last_name= user['last_name'], email= user['email'], password= user['password'], birthday=user['birthday'])
    print 'user sucessfully registered!!!'
    print user.first_name
    request.session['user'] = user.first_name
    messages.add_message(request, messages.SUCCESS, "The email address you enetered (" + request.POST['email'] + ") is a VALID email address! Thank you!")
    del request.session['first_name']
    del request.session['last_name']
    del request.session['email']
    del request.session['birthday']
    return redirect('/success')
def login(request):
    request.session['email1'] = request.POST['email1']
    user = User.userManager.login(request.POST['email1'], request.POST['password1'])
    if 'errors' in user:
        messages.add_message(request, messages.ERROR, 'Invalid Email/Password Combination.')
        return redirect('/')
    user = user['user']
    request.session['user']= user.first_name
    del request.session['email1']
    return redirect('/success')
def success(request):
    print 'logged in user... ->'
    print request.session['user']
    return render(request, 'loginreg_app/success.html')
def logout(request):
    del request.session['user']
    return redirect('/')
