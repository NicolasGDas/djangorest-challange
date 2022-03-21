from calendar import monthrange
from operator import mod
from django.http import JsonResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from products.models import Product
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instances = Product.objects.all()
    instance_1 = instances[0]
    # instance_2 = instances[1]
    data = {}
    if instances:
        data['1'] = ProductSerializer(instance_1).data
        # data['2'] = ProductSerializer(instance_2).data
    return Response(data)