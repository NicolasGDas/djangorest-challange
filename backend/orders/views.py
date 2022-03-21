import json
from math import prod
from rest_framework import  viewsets
from orders_details.models import OrderDetail
from .models import Order
from .serializers import OrderSerializer,OrderOrderDetailInlineSerializer
from orders_details.serializers import OrderDetailModifySerializer
import requests
from rest_framework.response import Response
from api.authentication import get_JTKAuth
# Create your views here.

class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    lookup_field = 'pk'
    
    def get_serializer_class(self):
        return OrderSerializer

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        data_order = (OrderOrderDetailInlineSerializer(order.order.all(), many=True).data)
        order_detail_ingresado = request.data["orderDetails"]

        for prodDB in data_order:
            for orderDetail in order_detail_ingresado:
                if not dict(dict(prodDB)['product'])['pk'] == orderDetail['product']['pk']:
                    data = {
                        "cuantity": orderDetail['cuantity'],
                        "order": order.id,
                        "product": str(orderDetail['product']['pk'])
                    }
                    
                    requests.post("http://localhost:8000/api/ordersDetails/",json=data,headers=get_JTKAuth())
                else:
                    pk = dict(prodDB)['pk']
                    data = {
                        "cuantity": orderDetail['cuantity'],
                        "order": order.id,
                        "product": str(orderDetail['product']['pk'])
                    }
                    endpoint = f"http://localhost:8000/api/ordersDetails/{pk}/"
                    requests.put(endpoint,json=data,headers=get_JTKAuth())
                    
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        new_order = Order.objects.create()
        new_order.save()
        order_detail_post = request.data["orderDetails"]
        for orderDetail in order_detail_post:
            data = {
                "cuantity": orderDetail['cuantity'],
                "order": new_order.id,
                "product": str(orderDetail['product']['pk'])
            }
            response = requests.post("http://localhost:8000/api/ordersDetails/",json=data,headers=get_JTKAuth())
            print(response.status_code)
            if response.status_code == 400:
                Order.objects.filter(id__exact = new_order.id).delete()
                return Response(response.json())
        serializer = OrderSerializer(new_order)

        return Response(serializer.data)


