from statistics import mode
from rest_framework import serializers

from orders_details.serializers import OrderDetailListSerializer,OrderDetailPublic
from .models import Order
from products.serializers import ProductPublicSerializer


class OrderOrderDetailInlineSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    cuantity = serializers.IntegerField(read_only = True)
    product = ProductPublicSerializer(read_only = True)

    




class OrderPublicSerializer(serializers.Serializer):
    id = serializers.CharField(read_only = True)
    fecha = serializers.DateField(read_only = True)



#Serializer para mostrar ordenest
class OrderSerializer(serializers.ModelSerializer):
    orderDetails = serializers.SerializerMethodField(read_only = True)
    total_pesos = serializers.SerializerMethodField(read_only = True)
    total_dolars = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Order
        fields = [
            'pk',
            'datetime',
            'total_pesos',
            'total_dolars',
            'orderDetails',
        ]

    def get_total_pesos(self,obj):
        total_pesos = 0
        for i in obj.order.all():
            precio_producto = i.product.price #Precio del producto de esta orderDetail
            cuantity = i.cuantity
            total_detail = float(obj.get_total_pesos(precio_producto,cuantity)) #precio total del detail
            total_pesos = total_pesos + total_detail
        return total_pesos
    
    
    def get_total_dolars(self,obj):
    
        return float(obj.get_total_usd(self.get_total_pesos(obj)))

    
    def get_orderDetails(self,obj):
        my_orderDetails_qs = obj.order.all()
        return OrderOrderDetailInlineSerializer(my_orderDetails_qs, many=True, context=self.context).data



    
