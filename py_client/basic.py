import json
from turtle import end_poly
import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint)
print (get_response.json())