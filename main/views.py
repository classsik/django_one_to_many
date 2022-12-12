from django.shortcuts import render
from .models import Product, Company
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import ProductForm


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create(request):
    create_companies()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request, 'create.html', {'form': form})


def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        form = ProductForm(instance=product)
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"form": form})
    except Product.DoesNotExist:
        return HttpResponseNotFound(" <h2›Product not found</h2>")


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name="Apple")
        Company.objects.create(name="Asus")
        Company.objects.create(name="MSI")
