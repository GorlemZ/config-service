from peewee import *
import os

DATABASE_URI = os.getenv('DATABASE_URI')

db = PostgresqlDatabase('mytest', host='localhost', port=5432, user='postgres', password='mysecretpassword')

#
# db = PostgresqlDatabase(DATABASE_URI)

db.connection()

class ConfigDataIn(Model):
   name=TextField()
   value=TextField()
   class Meta:
      database=db
      db_table='ConfigDataIn'


db.create_tables([ConfigDataIn])