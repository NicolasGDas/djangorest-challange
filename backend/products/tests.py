from rest_framework import status
from django.urls import reverse
from api.tests import setUP



class TestListGetProducts(setUP):
    
#-------------------------------------Tests w/o auth-------------------------------------
    def test_add_prod_wo_auth(self):
        prod = self.create_product().json()
        response = self.client.post(reverse("products-list"),prod)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_products_wo_auth(self):
        response = self.client.get(reverse("products-list"))
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_put_products_wo_auth(self):
        data = {
            'stock': 5
        }
        response = self.client.put(reverse("products-detail",args="1"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)



    def test_delete_products_wo_auth(self):
        url = reverse("products-detail",kwargs = {'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_update_stock_wo_auth(self):
        data = {
            'stock': 5
        }
        url = reverse("products-detail",args="1")
        response = self.client.patch(f'{url}update_stock/',data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)


#-------------------------------------Tests with auth-------------------------------------

    def test_add_product_with_data(self):
        self.authenticate()
        prod = {
            'name': "Product 1",
            'stock': 3,
            'price' :150
        }
        response = self.client.post(reverse("products-list"),prod)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'],prod["name"])
        self.assertEqual(response.data['price'],prod["price"])
        self.assertEqual(response.data['stock'],prod["stock"])

    def test_add_product_without_data(self):
        self.authenticate()
        response = self.client.post(reverse("products-list"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_put_products_with_auth(self):
        self.authenticate()
        data = {
        'name': "Cambiado",
        'stock': 5,
        'price': 34
        }
        self.create_product()
        response = self.client.put(reverse("products-detail",args="1"),data)
        self.assertEqual(response.data['name'],data["name"])
        self.assertEqual(response.data['price'],data["price"])
        self.assertEqual(response.data['stock'],data["stock"])
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        



    def test_delete_products_with_auth(self):
        self.authenticate()
        prod = self.create_product()
        url = reverse("products-detail",kwargs = {'pk': prod.json()['pk']})
        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_update_stock_with_auth_valid_data(self):
        self.authenticate()
        data = {
            'stock': 3
        }
        prod = self.create_product().json()
        stock_antes = prod['stock']
        url = reverse("products-detail",args=str(prod['pk']))
        response = self.client.patch(f'{url}update_stock/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_stock_with_auth_not_valid_data(self):
        self.authenticate()
        data = {
            'name': "Pepe"
        }
        prod = self.create_product().json()
        url = reverse("products-detail",args=str(prod['pk']))
        response = self.client.patch(f'{url}update_stock/',data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    

