import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.catalog, name='index'),
    path('<int:pk>', mainapp.catalog, name='products'),
]
