from fastapi import FastAPI
from fastapi.testclient import TestClient
import main
from peewee import *
import os


client = TestClient(main.app)

def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}


