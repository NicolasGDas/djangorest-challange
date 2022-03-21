
# from decimal import Decimal
# from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

unique_product_name = UniqueValidator(queryset=Product.objects.all(), lookup='iexact')

# def valid_price_number(value):
    
#     if ',' in str(value):
#         raise serializers.ValidationError("Tiene coma")
#     return(value)

