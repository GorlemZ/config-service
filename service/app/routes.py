from typing import List
from fastapi import APIRouter, HTTPException
from app.db import ConfigDataDB
from app.models import ConfigDataAPI

service = APIRouter()

@service.get('/health', status_code=200)
def health_endpoint():
    return {"Awesome!": "The API is LIVE!!"}

@service.get('/get-conf-item/{item_name}', status_code=200)
def find_a_config_by_unique_name(item_name: str):
# Considering a SOA, could be useful to validate the get request
# on the base of the client host, for best loose coupling data management 
# see comment on db.py 
    #client_host= request.client.host
    try:
        data=ConfigDataDB.get(ConfigDataDB.servicename == item_name)
        return ConfigDataAPI(servicename=data.servicename, value=data.value)
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{item_name} not found")

@service.get('/get-all-servicenames', status_code=200)
def get_all():
    all= list(ConfigDataDB.select(ConfigDataDB.servicename))
    return {'servicenames': [x.servicename for x in all]}

#for this endpoint could be a good idea to add different status_codes for updated and created 
@service.post('/upsert', status_code=200)
async def create_or_update_a_configuration_item(item: ConfigDataAPI):

    (getquery, bool)= ConfigDataDB.get_or_create(servicename=item.servicename, value = item.value)
    if(bool):
        return {getquery.servicename: 'created'}
    else:
        upquery=ConfigDataDB.update({ConfigDataDB.value: item.value}).where(ConfigDataDB.servicename==item.servicename ).execute()
        if(upquery>0):
            return {getquery.servicename: 'updated'}
        else:
            raise HTTPException(status_code=500, detail="something went wrong")

