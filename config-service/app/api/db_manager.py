from app.api.models import ConfigDataIn, ConfigDataOut, ConfigDataUpdate
from app.api.db import database, configs

async def add_config_data(payload: ConfigDataIn):
    query = configs.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_configs():
    query = configs.select()
    return await database.fetch_all(query=query)

async def get_config_data(id):
    query = configs.select(configs.c.id==id)
    return await database.fetch_one(query=query)

async def delete_config_data(id: int):
    query = configs.delete().where(configs.c.id==id)
    return await database.execute(query=query)

async def update_config_data(id: int, payload: ConfigDataIn):
    query = (
        configs
        .update()
        .where(configs.c.id == id)
        .values(**payload.model_dump())
    )
    return await database.execute(query=query)