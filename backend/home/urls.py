"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api/',include('api.urls')),
    #La agrego aca para comodidad, pero en caso de tener que usar mas cosas que esta api que implementamos podria
    #meter este path en la carpeta de api.urls y seria lo mismo y quedaria
    # mas limpio esta lista 
    #  Quedo comentado como seria en api.urls 
    # path('api/products/',include('products.urls')),
    

]
