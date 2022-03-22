from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
pk = 1
class setUP(APITestCase):
    def authenticate(self):
        userTest = User.objects.create_superuser('test_user',password="123")
        self.client.force_login(user=userTest)
        data = {
            "username": userTest.get_username(),
            'password':"123"
        }
        response = self.client.post(reverse("token_obtain_pair"),data)
        token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {token}')
    
    
    def create_product(self):
        response = self.client.post(reverse("products-list"),{
            "name": f"Producto {pk}",
            "price": 150.5,
            "stock": 10
        })
        return response
    
    
    def create_orderDetail(self):
        response = self.client.post(reverse("orderDetail-list"),{
            "cuantity": 1,
            "order": "1",
            "product": "1"
        })
        return response
    
    def create_order_with_details(self):
        response = self.client.post(reverse("orders-list"),{
            "orderDetails":[
                {
                    "cuantity": 1,
                    "product": {
                        "pk": 1
                    }
                }
            ]
        })
        return response

    def create_order_wo_details(self):
        response = self.client.post(reverse("orders-list"))
        return response

