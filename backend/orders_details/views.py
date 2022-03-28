from rest_framework.response import Response
from rest_framework import  viewsets
from .models import OrderDetail
from .serializers import OrderDetailListSerializer,OrderDetailModifySerializer
from rest_framework import status
from products.models import Product

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
        
        oDetail = self.get_object()
        product = oDetail.product
        product.increment_stock(oDetail.cuantity)
        product.save()

        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        product = obj.product

        if request.data.get('cuantity'):
            product.increment_stock(obj.cuantity)
            product.save()
            if int(product.get_stock()) >= int(request.data.get('cuantity')):
                product.decrement_stock(int(request.data.get('cuantity')))
                product.save()
            else:
                return Response("No hay suficiente stock, stock acutal{}".format(product.get_stock()),status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        
        product = Product.objects.filter(id__exact=request.data.get('product'))[0]
        if request.data.get('cuantity') <= product.get_stock():
            product.decrement_stock(request.data.get('cuantity'))
            product.save()
        else:
            return Response("No hay suficiente stock. Stock actual: {}".format(product.get_stock()),status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
    