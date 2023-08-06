from typing import List
from fastapi import APIRouter, HTTPException

from app.db import ConfigDataIn
from app.db import ConfigDataOut

service = APIRouter()

@service.get('/health', status_code=201)
def health():
    return (ConfigDataOut)

@service.post('/', status_code=201)
def add_config(payload: str):
    g= (ConfigDataIn
       .insert( name='Gianni', value = payload)
       .execute())
    return g