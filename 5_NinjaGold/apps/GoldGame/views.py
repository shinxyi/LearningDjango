from django.shortcuts import render, redirect
import random
from time import localtime, strftime

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activities']= []
    return render(request, 'GoldGame/index.html')
def process(request, path):
    if request.method == 'POST':
        location = {
            'farm':random.randint(10,20),
            'cave':random.randint(5,10),
            'house':random.randint(2,5),
            'casino':random.randint(-50,50),
        }
        if path in location:
            result = location[path]
            request.session['gold'] = request.session['gold'] + result
            result_dictionary = {
                                    'activity': ("Entered a casino and lost {} gold(s)... Ouch..".format(result),
                                    "Earned {} gold(s) from the {}!".format(result, path))[result>0],
                                    'time': strftime("%Y/%m/%d %I:%M %p", localtime())
                                }
            request.session['activities'].insert(0,str(result_dictionary['activity'])+ " ( " + str(result_dictionary['time']) + " ) ")
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')
