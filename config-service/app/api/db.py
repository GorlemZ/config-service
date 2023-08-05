from peewee import *
import os

DATABASE_URI = os.getenv('DATABASE_URI')
db = PostgresqlDatabase(DATABASE_URI)

class ConfigDataIn(Model):
   name=TextField()
   last_update=DateField()
   is_prod= BooleanField()
   value=TextField()
   class Meta:
      database=db
      db_table='ConfigDataIn'
      
db.create_tables([ConfigDataIn])