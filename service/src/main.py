from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from .api.routes import service
from .api.db import db
import os

app = FastAPI(openapi_url="/api/v1/configdataservice/openapi.json", docs_url="/api/v1/configdataservice/docs")

@app.on_event("shutdown")
def shutdown():
    db.close()
    

app.include_router(service, prefix='/api/v1/configdataservice')

#from docker
#http://localhost:8001/api/v1/configdataservice/docs

#from local
#http://localhost:8000/api/v1/configdataservice/docs