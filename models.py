from peewee import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    FloatField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimeField,
    UUIDField
)

import settings

db = SqliteDatabase(settings.DB_NAME, pragmas={'cache_size': 0})


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    phone = CharField()
    age = IntegerField()
    male = BooleanField()


class GodModel(BaseModel):
    is_god = BooleanField()
    name = CharField(max_length=150)
    years = IntegerField()
    date_birth = DateField()
    date_time_birth = DateTimeField()
    divine_value = FloatField()
    divine_description = TextField()
    replenish_divine_time = TimeField()
    divine_uuid = UUIDField()


if __name__ == '__main__':
    tables = [Person, GodModel]

    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)
