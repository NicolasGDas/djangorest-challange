from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
import json


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Token'

def get_JTKAuth():
    creds = open('..\py_client\creds.json',"r")
    token = json.loads(creds.read())['access']
    headers= {
        "Authorization": f"Bearer {token}"
            }
    return headers