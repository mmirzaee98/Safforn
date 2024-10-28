from django.shortcuts import render
from shop.models import Product

def category(request):
    return render(request, 'category.html')

def checkout(request):
    return render(request, 'checkout.html')

def product(request, pk):
    p = Product.objects.get(pk=pk)
    return render(request, 'product.html',{'product': p})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
