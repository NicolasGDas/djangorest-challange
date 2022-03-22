from ast import Or
from cgitb import lookup
from dataclasses import field
from itertools import product
from rest_framework import serializers
from .models import OrderDetail,Order
from .models import Product
from .models import Order
from products.serializers import ProductPublicSerializer
# from orders.serializers import OrderPublicSerializer

class OrderDetailPublic(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    cuantity = serializers.IntegerField(read_only = True)
    product = ProductPublicSerializer(read_only = True)

#Serializer para listar las ordersDetails
class OrderDetailListSerializer(serializers.ModelSerializer):
    product = ProductPublicSerializer(read_only = True)
    # order = OrderPublicSerializer(read_only = True)
    class Meta:
        model = OrderDetail
        fields = [
            'pk',
            'cuantity',
            'order',
            'product',
        ]

#Serializer para cuando queres agregar una ordenDetail
class OrderDetailModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = [
            'pk',
            'cuantity',
            'order',
            'product',
        ]
    def validate(self, attrs):
        id = attrs['product'].id
        product = (Product.objects.filter(id__exact = id)).values()
        print(attrs['cuantity'])
        if attrs['cuantity'] <= 0:
            raise serializers.ValidationError("La cantidad no puede ser 0")
        if product[0]['stock'] < attrs['cuantity']:
            raise serializers.ValidationError("No hay suficiente stock")


        return super().validate(attrs)



    def create(self, validated_data):
        # print(validated_data)
        product = validated_data.pop('product')
        cuantity =validated_data.pop('cuantity')
        product.decrement_stock(cuantity)
        product.save()
        validated_data["product"] = (product)
        validated_data["cuantity"] = (cuantity)
        # print(validated_data)
        return super().create(validated_data)
