from peewee import *
import os

isTest=True

USER= os.getenv('POSTGRES_USER')
PSW= os.getenv('POSTGRES_PASSWORD')
DB= os.getenv('POSTGRES_DB_T') if isTest else os.getenv('POSTGRES_DB')
HOST= 'conf_db'
PORT= 5432

db= PostgresqlDatabase(DB, host=HOST, port=PORT, user=USER, password=PSW)


class ConfigDataIn(Model):
    name= CharField(max_length=200)
    value= CharField(max_length=200)
    class Meta:
      database=db
      db_table='ConfigDataIn'

class ConfigDataOut(Model):
    name= CharField(max_length=200)
    value= CharField(max_length=200)
      
db.create_tables([ConfigDataIn])