from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
from peewee import *
import os


client = TestClient(app)

def test_root():
    response = client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "The API is LIVE!!"}


