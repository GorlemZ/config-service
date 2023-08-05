from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ConfigDataIn, ConfigDataOut, ConfigDataUpdate

service = APIRouter()

@service.get('/health', response_model=List[ConfigDataIn])
def health():
    print('health endpoint')

@service.post('/', status_code=201)
async def add_config(payload: ConfigDataIn):
    return {'id': 1}