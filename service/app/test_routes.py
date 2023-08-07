import pytest
from fastapi.testclient import TestClient
from app.main import app
from peewee import *
from app.db import ConfigDataDB
from app.models import ConfigDataAPI
import random
import string


client = TestClient(app)
data=[
        {'servicename': 'service1', 'value': 'moreconfig'},
        {'servicename': 'service2', 'value':   '{"title": "example glossary", "other": "moreconfigagain"}'}
    ]

def test_health():
    response = client.get("/api/v1/configdataservice/health")
    assert response.status_code == 200
    assert response.json() == {"Awesome!": "The API is LIVE!!"}
    
def test_get_all():
    response = client.get("/api/v1/configdataservice/get-all-servicenames")
    assert response.status_code == 200
    assert response.json() == {
    "servicenames": [
        "service1",
        "service2"
        ]
    }
    
def test_get1():
    response = client.get("/api/v1/configdataservice/get-conf-item/service1")
    assert response.status_code == 200
    assert response.json() == data[0]
    
def test_get2():
    response = client.get("/api/v1/configdataservice/get-conf-item/service2")
    assert response.status_code == 200
    assert response.json() == data[1]
    
def test_get_err():
    response = client.get("/api/v1/configdataservice/get-conf-item/service24")
    assert response.status_code == 404
    assert not response.json().get('detail') is None
    assert "service24" in response.json().get('detail') 

def test_post_created_updated():
    name= ''.join(random.choices(string.ascii_lowercase, k=10))
    input= ConfigDataAPI(servicename=name, value=str(data[0])).model_dump_json()
    response = client.post("/api/v1/configdataservice/upsert", content=input)
    assert response.status_code == 200
    assert response.json() == {name: 'created'}
    response_check = client.get(f"/api/v1/configdataservice/get-conf-item/{name}")
    assert response_check.status_code == 200
    
def test_post_updated():
    name= ''.join(random.choices(string.ascii_lowercase, k=10))
    input= ConfigDataAPI(servicename=name, value=str(data[1])).model_dump_json()
    response = client.post("/api/v1/configdataservice/upsert", content=input)
    assert response.status_code == 200
    response2 = client.post("/api/v1/configdataservice/upsert", content=input)
    assert response2.status_code == 200
    assert response2.json() == {name: 'updated'}
    
@pytest.fixture(autouse=True)
def run_around_tests():
    for d in data:
        ConfigDataDB.get_or_create(servicename=d["servicename"], value=d["value"])  
        
    yield
    
    ConfigDataDB.delete().execute()