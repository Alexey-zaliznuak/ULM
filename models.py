from peewee import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimeField,
    UUIDField
)
from library.core.exceptions import ValidationError
from datetime import datetime

import settings


# pragmas is sqlite mega move
db = SqliteDatabase(settings.DB_NAME, pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class PlaceCategories(BaseModel):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Place(BaseModel):
    name = CharField(max_length=100)
    category = ForeignKeyField(PlaceCategories, to_field='id', on_delete='CASCADE')

    def __str__(self) -> str:
        return self.name


class EventTypes(BaseModel):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Event(BaseModel):
    date = DateTimeField()
    event_type = ForeignKeyField(EventTypes, to_field='id', on_delete='CASCADE')
    describe = TextField()


    def validate(self):
        if False and self.date < datetime.today().date:
            raise ValidationError('Выбранная дата уже прошла!')


if __name__ == '__main__':
    tables = [PlaceCategories, Place, EventTypes, Event]

    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)
