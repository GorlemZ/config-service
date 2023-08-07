from peewee import *
import os

isTest=True

USER= 'conf_db_username' if isTest else os.getenv('POSTGRES_USER')
PSW= 'conf_db_password' if isTest else os.getenv('POSTGRES_PASSWORD')
DB= 'test' if isTest else os.getenv('POSTGRES_DB')
HOST= 'localhost' if isTest else 'conf_db'

db= PostgresqlDatabase(DB, user=USER, password=PSW, host=HOST, port=5432)

# I would study peewee library to understand how id indexing is managed 
# when not mapped in the model: is it retrievable nonetheless?
# Data Structure: for best data separation practice, I would add an
# env attribute to the table, like "staging", "prod" 

class ConfigDataDB(Model):
    servicename= CharField(max_length=200, unique=True)
    value= CharField(max_length=200)
    class Meta:
      database=db
      table_name='ConfigDataDB'
      
db.create_tables([ConfigDataDB])