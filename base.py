from peewee import *
db = SqliteDatabase ('musichub.db')

class Persona(Model):
    username = CharField()
    nombrecompleto = CharField()
    email = CharField()
    contrasena = CharField()
    edad = IntegerField(default=0)
    telefono = IntegerField(default=0)
    instrumentos = CharField(null=True)
    bio = TextField(null=True)

    class Meta():
        database = db

def create_and_connect():
    db.connect()
    db.create_tables([Persona],safe=True)

create_and_connect()
