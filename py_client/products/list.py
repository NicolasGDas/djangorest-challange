from inspect import EndOfBlock
import json
from wsgiref import headers
import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"
# password = getpass()
#remplazar para token
auth_response = requests.post(auth_endpoint, json={'username':'nicog','password': "123"})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint,headers=headers)
    print (get_response.json())