import os
import sys
from peewee import (
    # BooleanField,
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
    # big = BooleanField(
    #     default=False,
    #     help_text='Может вместить 2 мероприятия одновременно'
    # )

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

    def validate(self, create=False):
        if create:
            if self.date < datetime.today() - timedelta(days=1):
                raise ValidationError('Выбранная дата уже прошла!')

    def __str__(self) -> str:
        return self.describe


class WorkType(BaseModel):
    name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TasksStatuses(BaseModel):
    status_name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.status_name


class Task(BaseModel):
    date_registration = DateTimeField()
    event = ForeignKeyField(Event, to_field='id', on_delete='CASCADE')
    work_type = ForeignKeyField(WorkType, to_field='id', on_delete='CASCADE')
    place = ForeignKeyField(Place, to_field='id', on_delete='CASCADE')
    deadline = DateTimeField()

    describe = TextField()
    status = ForeignKeyField(
        TasksStatuses, to_field='id', on_delete='CASCADE'
    )

    def validate(self, create=False):
        if self.date_registration > self.deadline:
            raise ValidationError(
                'Срок должен быть позже даты создания.'
            )

    def __str__(self) -> str:
        return f"Task at {self.date_registration}"


class Booking(BaseModel):
    date_creation = DateTimeField()
    event = ForeignKeyField(Event, to_field='id', on_delete='CASCADE')

    def validate(self, create=False):
        if self.date_creation > self.deadline:
            raise ValidationError(
                'Срок должен быть позже даты создания.'
            )

    def __str__(self) -> str:
        return f"Task at {self.date_registration}"


def init_tables():
    tables = [
        Categories,
        Place,
        EventTypes,
        Event,
        TasksStatuses,
        WorkType,
        Task
    ]

    def remake_db():
        print('create')
        db.connect()
        db.drop_tables(tables)
        db.create_tables(tables)
        from generators import generate
        generate()

    if '--make' in sys.argv:
        remake_db()
        return

    if os.path.exists('./db.db'):
        try:
            db.connect()
        except Exception:
            pass
        if __name__ == '__main__':
            db.drop_tables(tables)
        db.create_tables(tables)
    else:
        remake_db()


if __name__ == '__main__':
    init_tables()
