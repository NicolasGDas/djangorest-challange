from rest_framework import status
from django.urls import reverse
from api.tests import setUP


class TestOrderDetails(setUP):
    #-------------------------------------Tests w/o auth-------------------------------------
    def test_add_order_detail_wo_auth(self):
        data = {
            "cuantity": 1,
            "order": "88",
            "product": "9"
        }
        response = self.client.post(reverse("orderDetail-list"),data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_order_detail_wo_auth(self):
        response = self.client.get(reverse("orderDetail-list"))
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_put_order_detail_wo_auth(self):
        data = {
            "cuantity": 2,
        }
        response = self.client.put(reverse("orderDetail-detail",args="1"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)


    def test_delete_order_detail_wo_auth(self):
        url = reverse("orderDetail-detail",kwargs = {'pk': '1'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)



#-------------------------------------Tests with auth-------------------------------------

    def test_add_order_detail_with_auth(self):
        self.authenticate()
        product = self.create_product().json()
        order = self.create_order_wo_details().json()
        data = {
            "cuantity": 1,
            "order": str(order['pk']),
            "product": str(product['pk'])
        }
        response = self.client.post(reverse("orderDetail-list"),data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_order_detail_with_auth(self):
        self.authenticate()
        response = self.client.get(reverse("orderDetail-list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_put_order_detail_with_auth(self):
        self.authenticate()
        prod = self.create_product().json()
        order = self.create_order_wo_details().json()
        orderDetail = self.create_orderDetail().json()
        data = {
            'order': order['pk'],
            "cuantity": 2,
            "product": prod['pk']
        }
        old_stock = orderDetail['cuantity']
        url = reverse("orderDetail-detail",args=str(orderDetail['pk']))
        response = self.client.put(url,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)



    def test_delete_order_detail_with_auth(self):
        self.authenticate()
        prod = self.create_product().json()
        order = self.create_order_wo_details().json()
        orderDetail = self.create_orderDetail().json()
        url = reverse("orderDetail-detail",kwargs = {'pk': orderDetail['pk']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)