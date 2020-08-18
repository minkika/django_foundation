import json
import os
import random

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Product, ProductCategory
from basketapp.models import Basket

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
        'products': Product.objects.all()[:4],
        'new_products': Product.objects.all()[3:7],
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)

def new(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
        'products': Product.objects.all()[3:7],
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context)

def catalog(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    links_menu = ProductCategory.objects.all()
    category = {
        'name': 'All furniture'
    }

    if pk is None or pk == 0:
        products_list = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(category__pk=pk)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'copyright': 'Golubeva Lyubov - GB',
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'category': category,
        'products': products_list,
        'basket': basket
    }

    return render(request, 'mainapp/catalog.html', content)

def contacts(request):
    with open('mainapp/json/contact__locations.json') as f:
        json_data = json.load(f)
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'contacts',
        'contact_list': json_data['contacts'],
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request, pk):
    title = 'Product'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    links_menu = ProductCategory.objects.all()

    product = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(product)


    content = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/product.html', content)
