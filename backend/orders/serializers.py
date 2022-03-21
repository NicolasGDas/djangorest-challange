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



    



# class OrderDetailModifySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetail
#         fields = [
#             'pk',
#             'cuantity',
#             'product',
#         ]
#     def validate(self, attrs):
#         id = attrs['product'].id
#         product = (Product.objects.filter(id__exact = id)).values()
#         if attrs['cuantity'] <= 0:
#             raise serializers.ValidationError("La cantidad no puede ser 0")
#         if product[0]['stock'] < attrs['cuantity']:
#             raise serializers.ValidationError("No hay suficiente stock")
#         return super().validate(attrs)

#     def create(self, validated_data):
#         # print(validated_data)
#         product = validated_data.pop('product')
#         cuantity =validated_data.pop('cuantity')
#         product.update_stock(cuantity)
#         # product.save()
#         validated_data["product"] = (product)
#         validated_data["cuantity"] = (cuantity)
#         print(validated_data)
#         return super().create(validated_data)
# #serializer para CREAR o UDPATE orders
# class OrderCreateUdpateSerializer(serializers.ModelSerializer):
#     orderDetail = OrderDetailModifySerializer()
#     # test = serializers.SerializerMethodField()
#     class Meta:
#         model = Order
#         fields = [
#             'orderDetail'
#         ]

# class OrderDetailModifySerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = OrderDetail
#         fields = [
#             'pk',
#             'cuantity',
#             'product',
#             'order',
#         ]
#     def validate(self, attrs):
#         id = attrs['product'].id
#         product = (Product.objects.filter(id__exact = id)).values()
#         if attrs['cuantity'] <= 0:
#             raise serializers.ValidationError("La cantidad no puede ser 0")
#         if product[0]['stock'] < attrs['cuantity']:
#             raise serializers.ValidationError("No hay suficiente stock")

#         return super().validate(dict(attrs))


#     def create(self, validated_data):
#         print("Estoy en el create del order")
#         product = validated_data.pop('product')
#         cuantity =validated_data.pop('cuantity')
#         product.update_stock(cuantity)
#         product.save()
#         validated_data["product"] = (product)
#         validated_data["cuantity"] = (cuantity)
#         print(validated_data)
#         OrderDetail.objects.create(validated_data)
#         return validated_data

# class TestingOrder(serializers.ModelSerializer):
#     orderDetails = OrderDetailModifySerializer2()
#     class Meta:
#         model=Order
#         fields = [
#             'orderDetails',
#         ]

#     def create(self, validated_data):

#         orderDetailList = validated_data.pop('orderDetails')
#         # order = Order()
#         # order.save()
#         # print(order)
#         validated_data['orderDetails'] = orderDetailList
#         orderDetailList = dict(orderDetailList)
#         print(orderDetailList['order'].id)
#         # OrderDetailList['order'] = order
#         orderDetailSer = OrderDetailModifySerializer2(data=dict(orderDetailList))
#         print("Hola")
#         print(orderDetailSer.is_valid())
#         if orderDetailSer.is_valid():
#             orderDetailSer.save()
#         return validated_data

