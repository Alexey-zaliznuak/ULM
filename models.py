import os
import sys
from peewee import (
    BooleanField,
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
    name = CharField(max_length=100, help_text='Наименование пространства')
    category = ForeignKeyField(Categories, to_field='id', on_delete='CASCADE')
    big = BooleanField(
        default=False,
        help_text='Может вместить 2 мероприятия одновременно'
    )

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
    date_creation = DateTimeField(default=datetime.now)
    event = ForeignKeyField(Event, to_field='id', on_delete='CASCADE')
    start_booking_time = DateTimeField()
    end_booking_time = DateTimeField()

    # todo filter by queryset
    place = ForeignKeyField(Place, to_field='id', on_delete='CASCADE')
    book_full = BooleanField(
        help_text=(
            'Забронировать все помещение'
            '(если помещение может вместить только одно мероприятие, '
            'то можете проигнорировать этот параметр)'
        )
    )
    comment = TextField()

    def validate(self, create=False):
        if self.start_booking_time > self.end_booking_time:
            raise ValidationError(
                'Начало бронирование должно быть позже его конца.'
            )

        if self.date_creation > self.start_booking_time:
            raise ValidationError(
                'Указанная начальная дата бронирования уже прошла.'
            )

        # todo make normal algorithm
        bookings = Booking.select().where(
            Booking.place == self.place,
            Booking.start_booking_time < self.end_booking_time,
            Booking.end_booking_time > self.start_booking_time,
        )

        if bookings.count > 1:
            raise ValidationError(
                'Помещение уже полностью забронировано на это время'
            )
        if bookings.count == 1:
            if bookings[0].book_full:
                raise ValidationError(
                    'Помещение было полностью забронировано на это время'
                )
            if self.book_full:
                raise ValidationError(
                    'Невозможно забронировать полностью - '
                    'помещение уже частично забронировано.'
                )

    # todo check that it work)
    def clear_book_full(self, value):
        if not self.place.big:
            value = False

        return value

    def __str__(self) -> str:
        return f"Booking at {self.date_creation}"


def init_tables():
    tables = [
        Categories,
        Place,
        EventTypes,
        Event,
        TasksStatuses,
        WorkType,
        Task,
        Booking,
    ]

    def remake_db():
        print('create')
        try:
            db.connect()
        except Exception:
            pass
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
    print(Booking.event.name)
    # init_tables()
