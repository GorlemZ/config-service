from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from app.api.db import metadata, database, engine
from app.api.configs import service

metadata.create_all(engine)


app = FastAPI(openapi_url="/api/v1/configdataservice/openapi.json", docs_url="/api/v1/configdataservice/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(service, prefix='/api/v1/configdataservice')
