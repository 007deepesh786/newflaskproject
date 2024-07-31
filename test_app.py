import pytest
import json
from app import app

def test_get_all_products():
   response = app.test_client().get('/api/products')
   res = json.loads(response.data.decode('utf-8')).get("products")
   assert type(res[0]) is dict
   assert type(res[1]) is dict
   assert res[0]['ProductName'] == 'Iphone15Pro1'
   assert res[0]['Price'] == 90000.5
   assert response.status_code == 200
   assert type(res) is list