import mainapp.views as mainapp
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from geekshop import settings

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('product/', mainapp.product, name='product'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
