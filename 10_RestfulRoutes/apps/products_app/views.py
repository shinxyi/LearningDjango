from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context = { 'products': Product.objects.all() }
    return render(request, 'products_app/index.html', context)
def new(request):
    return render(request, 'products_app/new.html')
def create(request):
    print '***'
    print request.POST['name']
    print '***'
    request.session['name'] = request.POST['name']
    request.session['description'] = request.POST['description']
    request.session['price'] = request.POST['price']
    product = Product.objects.checkProduct(request.POST['name'], request.POST['description'], request.POST['price'])
    if 'errors' in product:
        for err in product['errors']:
            messages.add_message(request, messages.ERROR, err)
        return redirect(reverse('new'))
    product = product['product']
    Product.objects.create(name=product['name'], description=product['description'], price=product['price'])
    return redirect(reverse('index'))
def edit(request,id):
    context = { 'product': Product.objects.get(id=id) }
    return render(request, 'products_app/edit.html', context)
def show(request,id):
    context = { 'product': Product.objects.get(id=id) }
    return render(request, 'products_app/show.html', context)
def update(request,id):
    product = Product.objects.checkProduct(request.POST['name'], request.POST['description'], request.POST['price'])
    if 'errors' in product:
        for err in product['errors']:
            messages.add_message(request, messages.ERROR, err)
        return redirect(reverse('edit', kwargs={'id':id}))
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.price = request.POST['price']
    product.save()
    return redirect(reverse('show', kwargs={'id':id}))
def destroy(request,id):
    Product.objects.get(id=id).delete()
    return redirect(reverse('index'))
