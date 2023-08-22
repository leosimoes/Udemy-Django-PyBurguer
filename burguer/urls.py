from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('produto', views.detalhe_produto, name='produto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
