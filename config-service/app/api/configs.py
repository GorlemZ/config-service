from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ConfigDataIn, ConfigDataOut, ConfigDataUpdate

service = APIRouter()

fake_data_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'value': 'The surviving members of the resistance face the First Order once again.'
    }
]

@service.get('/', response_model=List[ConfigDataIn])
async def index():
    return fake_data_db

@service.post('/', status_code=201)
async def add_movie(payload: ConfigDataIn):
    data = payload.model_dump()
    fake_data_db.append(data)
    return {'id': len(fake_data_db) - 1}

