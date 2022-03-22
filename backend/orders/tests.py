from urllib import response
from rest_framework import status
from django.urls import reverse
from api.tests import setUP



class TestOrderDetails(setUP):
#-------------------------------------Tests w/o auth-------------------------------------
    def test_add_order_wo_auth(self):
        data = {
            "cuantity": 1,
            "order": "88",
            "product": "9"
        }
        response = self.client.post(reverse("orders-list"),data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_order_wo_auth(self):
        response = self.client.get(reverse("orders-list"))
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_put_order_wo_auth(self):
        data = {
            "cuantity": 2,
        }
        response = self.client.put(reverse("orders-detail",args="1"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)


    def test_delete_order_wo_auth(self):
        url = reverse("orders-detail",kwargs = {'pk': '1'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

#-------------------------------------Tests w/o auth-------------------------------------


    def test_add_order_wo_data(self):
        self.authenticate()
        response = self.client.post(reverse("orders-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_add_order_with_data(self):
        self.authenticate()
        prod = self.create_product().json()
        data = {
            "orderDetails":[
                {
                    "cuantity": 1,
                    "product": {
                        "pk": prod['pk']
                    }
                }
            ]
        }
        response = self.client.post(reverse("orders-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_order(self):
        self.authenticate()
        response = self.client.get(reverse("orders-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_order(self):
        self.authenticate()
        order = self.create_order_wo_details().json()
        url = reverse("orders-detail",kwargs = {'pk': order['pk']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_update_order(self):
        self.authenticate()
        prod = self.create_product().json()
        order = self.create_order_wo_details().json()

        data = {
            "orderDetails" : 
                {
                    "cuantity": 1,
                    "order": order['pk'],
                    "product": prod['pk']
                }
            
        }
        url = reverse("orders-detail",args= str(order['pk']))
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)