from pydantic import BaseModel

# pydantic + peewee : is it possible to encode one model into another?
# worth a look there, I don't like this double model data structure
class ConfigDataAPI(BaseModel):
    servicename: str
    value: str
