from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from peewee import *
from app.db import ConfigDataDB

client = TestClient(app)



data=[
        {'servicename': 'service1', 'value': 'moreconfig'},
        {'servicename': 'service2', 'value':   '{"title": "example glossary", "other": "moreconfigagain"}'}
    ]

for d in data:
    ConfigDataDB.get_or_create(servicename=d["servicename"], value=d["value"])
        

def test_health():
    response = client.get("/api/v1/configdataservice/health")
    assert response.status_code == 201
    assert response.json() == {"Awesome!": "The API is LIVE!!"}
    
def test_get():
    response = client.get("/api/v1/configdataservice/service1")
    assert response.status_code == 201
    assert response.json() == {'servicename': 'service1', 'value': 'moreconfig'}

