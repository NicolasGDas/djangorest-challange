
import requests


auth_endpoint = "http://localhost:8000/api/auth/"
# password = getpass()
#remplazar para token
auth_response = requests.post(auth_endpoint, json={'username':'nicog','password': "123"})


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

endpoint = "http://localhost:8000/api/products/1/" 

data = {
    "name" : "Producto 1",
    "price": 150.5,
    "stock": 4
}

get_response = requests.put(endpoint, json=data,headers=headers) 
# print(get_response.json())