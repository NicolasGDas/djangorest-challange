import json
import re
from rest_framework import  viewsets,serializers
from .models import OrderDetail
from .serializers import OrderDetailListSerializer,OrderDetailModifySerializer
from products.models import Product
import requests
from api.authentication import get_JTKAuth
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    # serializer_class = OrderDetailListSerializer
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderDetailListSerializer
        if self.action == 'retrive':
            return OrderDetailModifySerializer
        return OrderDetailModifySerializer

    def destroy(self, request, *args, **kwargs):
        
        details =(OrderDetail.objects.filter(id__exact = self.get_object().id).values()[0]) #[{'id': 54, 'order_id': 80, 'product_id': 10, 'cuantity': 1}]
        cuantity = details['cuantity']
        pk = details['product_id']
        data ={
            'cuantity' : cuantity
        }
        endpoint = f"http://localhost:8000/api/products/{pk}/"
        requests.patch(endpoint,json=data,headers=get_JTKAuth())

        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        product = obj.product

        if request.data.get('cuantity'):
            product.increment_stock(obj.cuantity)
            product.save()
            print(product.get_stock())
            if int(product.get_stock()) > int(request.data.get('cuantity')):
                product.decrement_stock(int(request.data.get('cuantity')))
                product.save()

        return super().update(request, *args, **kwargs)

    
    