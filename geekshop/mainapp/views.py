import json

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Product, ProductCategory


def main(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, pk=None):
    links_menu = ProductCategory.objects.all()
    category = {
        'name': 'All furniture'
    }

    if pk is None or pk == 0:
        products_list = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(category__pk=pk)

    return render(request, 'mainapp/catalog.html', {
        'copyright': 'Golubeva Lyubov - GB',
        'links_menu': links_menu,
        'category': category,
        'products': products_list,
    })

def contacts(request):
    with open('mainapp/json/contact__locations.json') as f:
        json_data = json.load(f)
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'contacts',
        'contact_list': json_data['contacts'],
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'product'
    }



    return render(request, 'mainapp/product.html', context)
