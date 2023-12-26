"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include  # Добавлен import include

import phones.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', phones.views.index),
    path('catalog/', phones.views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', phones.views.show_product, name='phone'),


# Добавлен include для включения URL-маршрутов приложения phones
#     path('phones/', include('phones.urls')),
# Другие маршруты вашего проекта...

]