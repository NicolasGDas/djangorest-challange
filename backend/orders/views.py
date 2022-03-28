from math import prod
from rest_framework import  viewsets
from orders_details.models import OrderDetail
from .models import Order
from .serializers import OrderSerializer,OrderOrderDetailInlineSerializer
from orders_details.serializers import OrderDetailModifySerializer
import requests
from rest_framework.response import Response
from api.authentication import get_JTKAuth
from rest_framework import status
from products.models import Product
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
        previus_detail = {}
        if request.data.get("orderDetails"):
            new_order = Order.objects.create()
            new_order.save()
            order_detail_post = request.data["orderDetails"]
            
            for orderDetail in order_detail_post:
                if not previus_detail:
                    previus_detail = orderDetail
                    self.create_details(orderDetail,new_order)
                elif not previus_detail.get('product').get('pk') == orderDetail['product']['pk']:
                    self.create_details(orderDetail,new_order)
                    previus_detail = orderDetail

            
            serializer = OrderSerializer(new_order)

            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response("No ingreso ningun detalle de order, ingrese uno por favor",status.HTTP_400_BAD_REQUEST)


    def create_details(self,orderDetail,new_order):
        data = {
                "cuantity": orderDetail['cuantity'],
                "order": new_order.id,
                "product": str(orderDetail['product']['pk'])
            }
        serializer = OrderDetailModifySerializer(data= data)
        if serializer.is_valid():
            print("is valid")
            serializer.save()
