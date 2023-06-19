import uuid
from peewee import *
import datetime

from config import Config
class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = DateField(default=datetime.datetime.now)
    
    class Meta:
        database = Config.DATABASE
        abstract = True

class Praca(BaseModel):
    nazwa = CharField()
    opis = CharField()
    deadline = DateField()
    taken = BooleanField(default=False)

class Zgloszenie(BaseModel):
    email = CharField()
    wiadomosc = CharField()
    nr_telefonu = CharField(null=True)
    praca = ForeignKeyField(Praca, backref='zgloszenia')

Config.DATABASE.create_tables([Praca, Zgloszenie])
