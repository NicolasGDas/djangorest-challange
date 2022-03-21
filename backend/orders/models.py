
from django.db import models
import requests
# Create your models here.

class Order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)

    def get_total_pesos(self,price,cuantity):
        total = price * cuantity
        return "{:.2f}".format(total)

    def get_total_usd(self,pesos):

        total_dolars = pesos / self.get_dolar_value()
        return "{:.2f}".format(total_dolars)

    def get_dolar_value(self):
        data_request = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales').json()
        dolar_value = next(item for item in data_request if item['casa']['nombre'] == "Dolar Blue")['casa']['venta']
        dolar_value = dolar_value.replace(",",".")
        dolar_value = float(dolar_value)
        return dolar_value