from peewee import *
import os

isTest=False

USER= os.getenv('POSTGRES_USER')
PSW= os.getenv('POSTGRES_PASSWORD')
DB= 'test' if isTest else os.getenv('POSTGRES_DB')
HOST= 'localhost' if isTest else 'conf_db'

db= PostgresqlDatabase(DB, user=USER, password=PSW, host=HOST, port=5432)


class ConfigDataDB(Model):
    id=IntegerField()
    servicename= CharField(max_length=200)
    value= CharField(max_length=200)
    class Meta:
      database=db
      table_name='ConfigDataDB'

      
db.create_tables([ConfigDataDB])