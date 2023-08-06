from peewee import *
import os

isTest=True

USER= os.getenv('POSTGRES_USER')
PSW= os.getenv('POSTGRES_PASSWORD')
DB= 'test' if isTest else os.getenv('POSTGRES_DB')

conn_url= f"postgresql://conf_db_username:conf_db_password@conf_db/{DB}"

db= PostgresqlDatabase(conn_url)


class ConfigDataDB(Model):
    id=IntegerField()
    servicename= CharField(max_length=200)
    value= CharField(max_length=200)
    class Meta:
      database=db
      constraints = [SQL('UNIQUE ("name" COLLATE NOCASE)')]
      table_name='ConfigDataDB'

      
db.create_tables([ConfigDataDB])