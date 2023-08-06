from typing import List
from fastapi import APIRouter, HTTPException, Request

from app.db import ConfigDataDB
from app.models import ConfigDataAPI
from fastapi.encoders import jsonable_encoder

service = APIRouter()

@service.get('/health', status_code=201)
def health():
    return {"Awesome!": "The API is LIVE!!"}

@service.get('/{item_name}', status_code=201)
def find(item_name: str):
#considering a SOA
#could be useful to validate the get request on the base of the client host
    #client_host= request.client.host
    try:
        data=ConfigDataDB.get(ConfigDataDB.servicename == item_name)
        return ConfigDataAPI(servicename=data.servicename, value=data.value)
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{item_name} not found")

@service.post('/', status_code=201)
async def create_item(item: ConfigDataAPI):

    (getquery, bool)= ConfigDataDB.get_or_create(servicename=item.servicename, value = item.value)
    if(bool):
        return {getquery.servicename: 'created'}
    else:
        upquery=ConfigDataDB.update({ConfigDataDB.value: item.value}).where(ConfigDataDB.servicename==item.servicename ).execute()
        if(upquery>0):
            return {getquery.servicename: 'updated'}
        else:
            raise HTTPException(status_code=501, detail="something went wrong")