
from rest_framework import serializers
import requests
from .models import Product
from .validators import unique_product_name



class ProductPublicSerializer(serializers.Serializer):
    name = serializers.CharField(read_only= False)
    pk = serializers.CharField(read_only= False)
    price = serializers.FloatField(read_only= False)
    stock = serializers.IntegerField(read_only= False)


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[unique_product_name])

    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'price',
            'stock',
        ]

  