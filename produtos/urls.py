"""
URL configuration for mercearias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from produtos import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.visualizarLoja, name='loja'),
    path('<slug:categoria_slug>/', views.visualizarLoja,
         name='produtos_por_categoria'),
    path('<slug:categoria_slug>/<slug:produto_slug>', views.visualizarDetalheProduto, name='visualizarDetalheProduto'),

]
