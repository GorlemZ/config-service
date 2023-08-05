from peewee import *
import os

isTest=False

USER= os.getenv('POSTGRES_USER') if isTest else os.getenv('POSTGRES_USER_T')
PSW= os.getenv('POSTGRES_PASSWORD') if isTest else os.getenv('POSTGRES_PASSWORD_T')
DB= os.getenv('POSTGRES_DB') if isTest else os.getenv('POSTGRES_DB_T')
HOST= 'conf_db' if isTest else 'conf_db_test'
PORT= 5433 if isTest else 5432

db= PostgresqlDatabase(DB, host=HOST, port=PORT, user=USER, password=PSW, autoconnect=False)

db.connect()


class ConfigDataIn(Model):
    name= CharField(max_length=200)
    value= CharField(max_length=200)
    class Meta:
      database=db
      db_table='ConfigDataIn'

      
db.create_tables([ConfigDataIn])