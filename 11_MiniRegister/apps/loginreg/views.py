from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages

# Create your views here.
def index(request):
    form = RegisterForm()
    form2 = LoginForm()
    context = {
        'myregistrationform': form,
        'myloginform': form2
    }
    return render(request, 'loginreg/index.html', context)
def register(request):
    # Confirm that the HTTP verb was a POST
    if request.method == "POST":
        if len(User.userManager.filter(email=request.POST['email']))>0:
            messages.add_message(request, messages.ERROR, 'Please check your email...')
            return redirect(reverse('index'))
        user = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
        if 'error' in user:
            messages.add_message(request, messages.ERROR, user['error'])
            return redirect(reverse('index'))
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            user = user['user']
            user = User.userManager.create(first_name= user['first_name'], last_name= user['last_name'], email= user['email'], password= user['password'])
            messages.add_message(request, messages.SUCCESS, "The email address you enetered (" + request.POST['email'] + ") is a VALID email address! Thank you!")
            request.session['user']= user.first_name
            return redirect(reverse('success'))
        else:
            print bound_form.errors
            for key in bound_form.errors:
                messages.add_message(request, messages.ERROR, bound_form.errors[key])
            return redirect(reverse('index'))
def login(request):
    if request.method == "POST":
        user = User.userManager.login(request.POST['email'], request.POST['password'])
        if 'errors' in user:
            messages.add_message(request, messages.ERROR, 'Invalid Email/Password Combination.')
            return redirect('/')
        user = user['user']
        print user.password
        request.session['user']= user.first_name
        return redirect(reverse('success'))
def success(request):
    return render(request, 'loginreg/success.html')
