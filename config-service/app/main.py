from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from app.api.configs import service
from app.api.db import db
import os


app = FastAPI(openapi_url="/api/v1/configdataservice/openapi.json", docs_url="/api/v1/configdataservice/docs")

#@app.on_event("startup")
#async def startup():
#    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    db.close()

app.include_router(service, prefix='/api/v1/configdataservice')

#http://localhost:8001/api/v1/configdataservice/docs