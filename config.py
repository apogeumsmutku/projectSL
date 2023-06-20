from peewee import SqliteDatabase

#config
class Config(object):
    DEBUG = False
    DATABASE = SqliteDatabase('zadania.db')
