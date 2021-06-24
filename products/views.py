from django.shortcuts import render

from products.models import Product, ProductCategory


# Create your views here.

def index(request):
    context = {
        'tittle': 'Geekshop - главная',
    }
    return render(request, 'products\index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context.update({'products': products})
    return render(request, 'products/products.html', context)
