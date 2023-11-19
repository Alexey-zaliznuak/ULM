import os
from peewee import (
    CharField,
    DateTimeField,
    DateTimeField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
    TextField,
)
from library.core.exceptions import ValidationError
from datetime import datetime, timedelta

import settings


# pragmas is sqlite mega move
db = SqliteDatabase(settings.DB_NAME, pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Categories(BaseModel):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Place(BaseModel):
    name = CharField(max_length=100)
    category = ForeignKeyField(Categories, to_field='id', on_delete='CASCADE')

    def __str__(self) -> str:
        return self.name


class EventTypes(BaseModel):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Event(BaseModel):
    category = ForeignKeyField(Categories, to_field='id', on_delete='CASCADE')
    date = DateTimeField()
    describe = TextField()
    event_type = ForeignKeyField(
        EventTypes, to_field='id', on_delete='CASCADE'
    )

    def validate(self):
        if self.date < datetime.today() - timedelta(days=1):
            raise ValidationError('Выбранная дата уже прошла!')


def init_tables():
    tables = [Categories, Place, EventTypes, Event]

    if os.path.exists('./db.db'):
        db.connect()
        if __name__ == '__main__':
            db.drop_tables(tables)
        db.create_tables(tables)
    else:
        db.connect()
        db.create_tables(tables)
        from generators import generate
        generate()


if __name__ == '__main__':
    init_tables()
