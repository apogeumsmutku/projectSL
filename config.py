from peewee import SqliteDatabase

#config
class Config(object):
    DEBUG = False
    DATABASE = SqliteDatabase('tasks.db')
