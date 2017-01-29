from django.shortcuts import render, redirect
import string, random

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    return render(request, 'word_gen/index.html')
def generate(request):
    if request.method == "GET":
        request.session['counter']+=1
        request.session['string']=''
        for i in range(0,14):
            let_or_int = random.randint(0,1)
            if let_or_int==1:
                request.session['string']+=random.choice(string.uppercase)
            else:
                request.session['string']+=str(random.randint(0,9))
        return redirect('/')
