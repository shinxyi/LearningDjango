from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        verify = True
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        if len(request.session['name']) < 1:
            messages.add_message(request, messages.INFO, 'Name field cannot be empty!')
            verify=False
        elif not request.session['name'].isalpha():
            messages.add_message(request, messages.INFO, 'Name can only contain letters!')
            verify=False

        if request.session['location']=='':
            messages.add_message(request, messages.INFO, 'Please pick a location!')
            verify=False
        if request.session['language']=='':
            messages.add_message(request, messages.INFO, 'Please pick a language!')
            verify=False

        if verify:
            if 'counter' not in request.session:
                request.session['counter']=0
            request.session['counter'] +=1
            messages.add_message(request, messages.SUCCESS, 'Thanks for submitting this form! You have submitted this form ' + str(request.session['counter']) + ' time(s) now.')
            return redirect('/result')

        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')

def reset(request):
    session_keys = list(request.session.keys())
    session_keys.remove('counter')
    print session_keys
    for key in session_keys:
        del request.session[key]
    return redirect('/')
