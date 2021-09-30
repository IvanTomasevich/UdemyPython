from peewee import *
from datetime import date


db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birtday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


def create_and_connect():
    db.connect()
    db.create_tables([Person, Pet], safe=True)


def create_family_members():
    uncle_tommy = Person(name="Tommy", birtday=date(2000, 11, 11), is_relative=True)
    uncle_tommy.save()

    grandma_ana = Person(name="Ana", birtday=date(1960, 4, 16), is_relative=False)
    grandma_rosa = Person(name="Rosa", birtday=date(1970, 6, 21), is_relative=False)

    tommys_dog = Pet.create(owner=uncle_tommy, name="Fido", animal_type="Dog")
    anas_cat = Pet.create(owner=grandma_ana, name="Pelusa", animal_type="Cat")

    tommys_dog.name = "Firulais"
    tommys_dog.save()


def get_family_members():
    for pernson in Person.select():
        print("Nombre: {} Fecha de cumpleaños: {}".format(pernson.name, pernson.birtday))


def get_family_member_birtday(name):
    grandma_rosa = Person.select().where(Person.name == "Rosa").get
    print("{} cumple el : {}".format(name, family_members.birtday))


create_and_connect()
get_family_members()
get_family_member_birtday("Rosa")
