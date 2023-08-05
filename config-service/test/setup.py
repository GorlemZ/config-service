from fastapi.testclient import TestClient
#from app.main import app
from peewee import *
import os

DATABASE_URI = os.getenv('T_URI')
db= PostgresqlDatabase(DATABASE_URI)
db = PostgresqlDatabase(
    'conf_db_dev_t', 
    user='conf_db_username_t', 
    password='test',  
    host='localhost',
    port='5433') 

class ConfigDataIn(Model):
   name=TextField()
   last_update=DateField()
   is_prod= BooleanField()
   value=TextField()
   class Meta:
      database=db
      db_table='ConfigDataIn'

db.create_tables([ConfigDataIn])

#client = TestClient(app)


