from pydantic import BaseModel
from typing import List, Optional

class ConfigDataIn(BaseModel):
    name: str
    value: str


class ConfigDataOut(ConfigDataIn):
    id: int


class ConfigDataUpdate(ConfigDataIn):
    name: Optional[str] = None
    value: Optional[str] = None