from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('products', viewset=views.ProductList,basename='products')


urlpatterns = [
    path('',include(router.urls)),
]