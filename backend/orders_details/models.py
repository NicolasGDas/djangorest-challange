
from django.db import models
from orders.models import Order
from products.models import Product
# Create your models here.
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cuantity = models.IntegerField()


    # def get_total_usd(self,valor_actual):
    #     return self.cuantity * valor_actual