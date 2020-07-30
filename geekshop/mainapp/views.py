import json

from django.shortcuts import render


def main(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def catalog_all(request):
    links_menu = [
        {'href': 'catalog_all', 'name': 'all'},
        {'href': 'catalog_home', 'name': 'home'},
        {'href': 'catalog_office', 'name': 'office'},
        {'href': 'catalog_modern', 'name': 'modern'},
        {'href': 'catalog_classic', 'name': 'classic'},
    ]
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'All furniture',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog_all.html', context)


def catalog_home(request):
    links_menu = [
        {'href': 'catalog_all', 'name': 'all'},
        {'href': 'catalog_home', 'name': 'home'},
        {'href': 'catalog_office', 'name': 'office'},
        {'href': 'catalog_modern', 'name': 'modern'},
        {'href': 'catalog_classic', 'name': 'classic'},
    ]
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'Home furniture',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog_all.html', context)


def catalog_office(request):
    links_menu = [
        {'href': 'catalog_all', 'name': 'all'},
        {'href': 'catalog_home', 'name': 'home'},
        {'href': 'catalog_office', 'name': 'office'},
        {'href': 'catalog_modern', 'name': 'modern'},
        {'href': 'catalog_classic', 'name': 'classic'},
    ]
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'Office furniture',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog_all.html', context)


def catalog_modern(request):
    links_menu = [
        {'href': 'catalog_all', 'name': 'all'},
        {'href': 'catalog_home', 'name': 'home'},
        {'href': 'catalog_office', 'name': 'office'},
        {'href': 'catalog_modern', 'name': 'modern'},
        {'href': 'catalog_classic', 'name': 'classic'},
    ]
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'Modern furniture',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog_all.html', context)


def catalog_classic(request):
    links_menu = [
        {'href': 'catalog_all', 'name': 'all'},
        {'href': 'catalog_home', 'name': 'home'},
        {'href': 'catalog_office', 'name': 'office'},
        {'href': 'catalog_modern', 'name': 'modern'},
        {'href': 'catalog_classic', 'name': 'classic'},
    ]
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'Classic furniture',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/catalog_all.html', context)


def contacts(request):
    with open('contact_list.json') as f:
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
