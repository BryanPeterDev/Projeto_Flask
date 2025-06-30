from peewee import Model,CharField,DateTimeField
from database.database import db
import datetime


class Cliente(Model):
    nome = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    data_registro = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db
