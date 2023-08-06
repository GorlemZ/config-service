from typing import List
from fastapi import APIRouter, HTTPException

from app.db import ConfigDataIn

service = APIRouter()

@service.get('/health', status_code=201)
def health():
    print({"message": "The API is LIVE!!"})

@service.post('/', status_code=201)
def add_config(payload: str):
    g= (ConfigDataIn
       .insert( name='Gianni', value = payload)
       .execute())
    return g