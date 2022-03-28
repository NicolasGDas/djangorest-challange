from posixpath import basename
from rest_framework import  viewsets
from .models import Product
from .serializers import ProductSerializer,ProductPublicSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def partial_update(self, request, *args, **kwargs):
        if request.data.get('cuantity'):
            request.data['stock'] = (self.get_object().stock + request.data.get('cuantity'))
            request.data.pop('cuantity')
        
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["patch"],basename="update_stock")
    def update_stock(self, request, pk=None, *args, **kwargs):

        if request.data.get('stock'):
            stock = request.data.get('stock') 
            if stock < 0:
                stock = 0
            product = self.get_object()
            product.update_stock(stock)
            product.save()
            response = ProductPublicSerializer(product)
        else:
            return Response("No ingreso stock para modificar",status= status.HTTP_400_BAD_REQUEST)

        return Response(response.data,status.HTTP_200_OK)