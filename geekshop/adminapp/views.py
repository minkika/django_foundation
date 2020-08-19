from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from authapp.models import ShopUser
from django.urls import reverse

from mainapp.models import ProductCategory

from mainapp.models import Product

from authapp.forms import ShopUserRegisterForm

from adminapp.forms import ShopUserAdminEditForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'admin / users'
    users_list = ShopUser.objects.all()
    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'users / create'
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}
    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'users / update'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method=='POST ':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)
    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'users / delete'

    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        if user_item.is_active:
            user_item.is_active = False
            user_item.save()
        else:
            user_item.is_active = True
            user_item.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user_item}
    return render(request, 'adminapp/user_delete.html', content)

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'admin / products'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item)
    content = {
        'title': title,
        'category': category_item,
        'objects': products_list
    }

    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'admin / category'
    categories_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    pass

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    pass
