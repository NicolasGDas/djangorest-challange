from django.db import models
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.IntegerField()


    def decrement_stock(self,value):
        self.stock = self.stock - value

    def get_stock(self):
        return self.stock

    def update_stock(self,new_stock):
        self.stock =  new_stock

    def increment_stock(self,increment):
        self.stock = self.stock + increment

