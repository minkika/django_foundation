import json

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
    title = 'All furniture'
    if pk:
        current_category = ProductCategory.objects.get(pk=pk)
        title = current_category.name
    links_menu = ProductCategory.objects.all()

    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog.html', context)

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
