
from django.shortcuts import render


def main(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'catalog',
    }
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', context)


def product(request):
    context = {
        'copyright': 'Golubeva Lyubov - GB',
        'title': 'product'
    }
    return render(request, 'mainapp/product.html', context)
