from pydantic import BaseModel


class ConfigDataAPI(BaseModel):
    servicename: str
    value: str
