import json
import requests
from posixpath import basename
from rest_framework import  viewsets
from .models import Product
from .serializers import ProductSerializer,ProductPublicSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from api.authentication import get_JTKAuth

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):

        return super().update(request, *args, **kwargs)
    

    def partial_update(self, request, *args, **kwargs):
        if request.data.get('cuantity'):
            request.data['stock'] = (self.get_object().stock + request.data.get('cuantity'))
            request.data.pop('cuantity')
        
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["patch"],basename="update_stock")
    def update_stock(self, request, pk=None, *args, **kwargs):

        if request.data.get('stock'):
            data = {
                'stock': request.data['stock']
            }
            endpoint = f"http://localhost:8000/api/products/{pk}/"
            retorno = requests.patch(endpoint,json=data,headers=get_JTKAuth())
        else:
            raise Exception("Por favor ingrese un stock para actualizar")


        return Response(retorno.json())









# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes =[
#         authentication.SessionAuthentication,    
#         TokenAuthentication
#     ]
#     permission_classes = [permissions.IsAdminUser]
#     def perform_create(self, serializer):
#         name = serializer.validated_data.get('name')
#         price = serializer.validated_data.get('price')
#         stock = serializer.validated_data.get('stock')

#         serializer.save()

# product_list_create_view = ProductListCreateAPIView.as_view()



# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_detail_view = ProductDetailAPIView.as_view()


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     # def perform_update(self, serializer):
#     #     instance = serializer.save()

# product_update_view = ProductUpdateAPIView.as_view()


# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)

# product_destroy_view = ProductDestroyAPIView.as_view()