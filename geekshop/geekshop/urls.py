"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('product/', mainapp.product, name='product'),
    path('catalog/all', mainapp.catalog_all, name='catalog_all'),
    path('catalog/home', mainapp.catalog_home, name='catalog_home'),
    path('catalog/office', mainapp.catalog_office, name='catalog_office'),
    path('catalog/modern', mainapp.catalog_modern, name='catalog_modern'),
    path('catalog/classic', mainapp.catalog_classic, name='catalog_classic'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]

