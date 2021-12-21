from django.test import TestCase
import requests
import json

data = {'card': 1234567891}
data_json = json.dumps(data)
res = json.loads(data_json)


r = requests.post('http://127.0.0.1:8000/bonus_account/get_account/', data=data_json)
print(r.text)

# Create your tests here.
