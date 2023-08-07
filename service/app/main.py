from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from app.routes import service
from app.db import db
import os

app = FastAPI(openapi_url="/api/v1/configdataservice/openapi.json", docs_url="/api/v1/configdataservice/docs")

@app.on_event("shutdown")
def shutdown():
    db.close()

app.include_router(service, prefix='/api/v1/configdataservice')

# THINGS I WOULD ADD:
#     - a better management of env vars with docker 
#     - after clarifications on the SOA services and the type of data needed, a DB refactoring:
#           should we add structured models of different configs?
#     - some kind of security assessment of the SOA, and more separation of responsibility for data retrieving
#     - no huge amount of requests shoud be due, so simple routing as this could be fine
#     
#http://localhost:8001/api/v1/configdataservice/docs
