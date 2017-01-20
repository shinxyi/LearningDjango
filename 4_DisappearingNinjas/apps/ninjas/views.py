from django.shortcuts import render, redirect


def index(request):
    return render(request, 'ninjas/index.html')
def showAll(request):
    context = {
        "img": "ninjas/images/tmnt.png"
    }
    return render(request, 'ninjas/show.html', context)
def show(request, word):
    if word == "blue":
        img = "ninjas/images/leonardo.jpg"
    elif word == "orange":
        img = "ninjas/images/michelangelo.jpg"
    elif word == "red":
        img = "ninjas/images/raphael.jpg"
    elif word == "purple":
        img = "ninjas/images/donatello.jpg"
    else:
        img = "ninjas/images/notapril.jpg"
    context = {
        "img": img
    }
    return render(request, 'ninjas/show.html', context)
