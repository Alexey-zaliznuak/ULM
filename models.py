import os
import sys
from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    DateField,
    TimeField,
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
    name = CharField(max_length=100, help_text='Наименование категории')

    def __str__(self) -> str:
        return self.name


class Place(BaseModel):
    name = CharField(max_length=100, help_text='Наименование пространства')
    category = ForeignKeyField(
        Categories,
        to_field='id',
        on_delete='CASCADE',
        help_text='Категория'
    )
    big = BooleanField(
        default=False,
        help_text='Может вместить 2 мероприятия одновременно'
    )

    def __str__(self) -> str:
        return self.name


class EventTypes(BaseModel):
    name = CharField(max_length=100, help_text='Наименование типа мероприятия')

    def __str__(self) -> str:
        return self.name


class Event(BaseModel):
    category = ForeignKeyField(
        Categories,
        to_field='id',
        on_delete='CASCADE',
        help_text='Категория'
    )
    date = DateField(help_text='Дата проведения')
    describe = TextField(help_text='Описание')
    event_type = ForeignKeyField(
        EventTypes,
        to_field='id',
        on_delete='CASCADE',
        help_text='Тип мероприятия'
    )

    def validate(self, create=False):
        if create:
            if self.date < datetime.today() - timedelta(days=1):
                raise ValidationError('Выбранная дата уже прошла!')

    def __str__(self) -> str:
        return self.describe


class WorkType(BaseModel):
    name = CharField(max_length=100, help_text='Дата проведения')

    def __str__(self) -> str:
        return self.name


class TasksStatuses(BaseModel):
    status_name = CharField(max_length=100, help_text='Нименование статуса')

    def __str__(self) -> str:
        return self.status_name


class Task(BaseModel):
    date_registration = DateTimeField()
    event = ForeignKeyField(
        Event,
        to_field='id',
        on_delete='CASCADE',
        help_text='Мероприятие'
    )
    work_type = ForeignKeyField(
        WorkType,
        to_field='id',
        on_delete='CASCADE',
        help_text='Вид работы'
    )
    place = ForeignKeyField(
        Place,
        to_field='id',
        on_delete='CASCADE',
        help_text='Помещение'
    )
    deadline = DateTimeField(help_text='Дедлайн')

    describe = TextField(help_text='описание')
    status = ForeignKeyField(
        TasksStatuses,
        to_field='id',
        on_delete='CASCADE',
        help_text='Статус'
    )

    def validate(self, create=False):
        if self.date_registration > self.deadline:
            raise ValidationError(
                'Срок должен быть позже даты создания.'
            )

    def __str__(self) -> str:
        return f"Task at {self.date_registration}"


class Booking(BaseModel):
    date_creation = DateTimeField(
        default=datetime.now,
        help_text='Дата создания'
    )
    event = ForeignKeyField(
        Event,
        to_field='id',
        on_delete='CASCADE',
        help_text='Мероприятие'
    )
    start_booking_time = DateTimeField(help_text='Начало бронирования')
    end_booking_time = DateTimeField(help_text='Окончание бронирования')

    # todo filter by queryset
    place = ForeignKeyField(
        Place,
        to_field='id',
        on_delete='CASCADE',
        help_text='Помешение'
    )
    book_full = BooleanField(
        help_text=(
            'Забронировать все помещение'
            '(если помещение может вместить только одно мероприятие, '
            'то значение будет установлено автоматически)'
        ),
    )
    comment = TextField(help_text='Комментарий')

    def validate(self, create=False):
        if not self.place.big:
            self.book_full = False

        if self.start_booking_time >= self.end_booking_time:
            raise ValidationError(
                'Начало бронирование должно быть раньше его конца.'
            )

        if self.date_creation.day > self.start_booking_time.day:
            raise ValidationError(
                'Указанная начальная дата бронирования уже прошла.'
            )

        # todo make normal algorithm
        bookings = Booking.select().where(
            Booking.place == self.place,
            Booking.start_booking_time <= self.end_booking_time,
            Booking.end_booking_time >= self.start_booking_time,
        )

        if bookings.count() > 1:
            raise ValidationError(
                'Помещение уже полностью забронировано на это время'
            )

        if bookings.count() == 1:
            if bookings[0].book_full or not self.place.big:
                raise ValidationError(
                    'Помещение было полностью забронировано на это время'
                )

            if self.book_full:
                raise ValidationError(
                    'Невозможно забронировать полностью - '
                    'помещение уже частично забронировано.'
                )

    def __str__(self) -> str:
        return f"Booking at {self.date_creation}"


class Teacher(BaseModel):
    full_name = CharField(max_length=100, help_text='ФИО Преподавателя')

    def __str__(self) -> str:
        return self.full_name


class ClubType(BaseModel):
    name = CharField(max_length=100, help_text='Наименование вида кружка')

    def __str__(self) -> str:
        return self.name


class Club(BaseModel):
    name = CharField(max_length=100, help_text='Наименование кружка')
    teacher = ForeignKeyField(
        Teacher,
        to_field='id',
        on_delete='CASCADE',
        help_text='Преподаватель'
    )
    club_type = ForeignKeyField(
        ClubType,
        to_field='id',
        on_delete='CASCADE',
        help_text='Вид кружка'
    )
    place = ForeignKeyField(
        Place,
        to_field='id',
        on_delete='CASCADE',
        help_text='Помещение'
    )
    date_start_working = DateField(help_text = 'Дата начала работы кружка')
    working_days = ...
    start_lesson_time = TimeField(help_text = 'Время конца занятия')
    end_lesson_time = TimeField(help_text = 'Время начала занятия')

    def __str__(self) -> str:
        return (
            self.name
            + ': '
            + str(self.start_lesson_time)
            + ' - '
            + str(self.end_lesson_time)
        )


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
    pass
    # print(Booking.event.name)
    # init_tables()
