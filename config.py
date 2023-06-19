from peewee import SqliteDatabase

class Config(object):
    DEBUG = False
    DATABASE = SqliteDatabase('zadania.db')
