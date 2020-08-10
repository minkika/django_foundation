from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('add/', basketapp.basket_add, name='add'),
]