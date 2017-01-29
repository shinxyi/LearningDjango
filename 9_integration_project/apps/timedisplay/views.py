from django.shortcuts import render, HttpResponse
from time import strftime,localtime

def showTime(request):
    date= strftime('%b %d, %Y', localtime())
    time= strftime('%I:%M %p')
    context = {
        "date":date,
        "time": time
    }
    return render(request,'timedisplay/page.html', context)
