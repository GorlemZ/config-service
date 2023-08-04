import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

configs = Table(
    'configs',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('value', String(50)),
)

database = Database(DATABASE_URI)