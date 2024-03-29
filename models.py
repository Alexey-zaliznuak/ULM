import os
import sys
from peewee import (
    CharField,
    IntegerField,
    ForeignKeyField,
    Model,
    SqliteDatabase,
    TextField,
)
import settings


# pragmas is sqlite mega move
db = SqliteDatabase(settings.DB_NAME, pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Place(BaseModel):
    name = CharField(max_length=100, help_text='Наименование пространства')
    capacity = IntegerField(help_text='Вместимость пространства')
    describe = TextField(help_text='Описание')

    def __str__(self) -> str:
        return self.name


class Studio(BaseModel):
    name = CharField(max_length=100, help_text='Наименование категории')
    describe = TextField(help_text='Описание')

    def __str__(self) -> str:
        return self.name


class Exhibit(BaseModel):
    name = CharField(max_length=100, help_text='Наименование пространства')
    studio = ForeignKeyField(
        Studio,
        to_field='id',
        on_delete='CASCADE',
        help_text='Владелец'
    )

    def __str__(self) -> str:
        return self.name


class Teacher(BaseModel):
    full_name = CharField(max_length=100, help_text='ФИО Преподавателя')

    def __str__(self) -> str:
        return self.full_name


#----------------------------------------
# class Categories(BaseModel):
#     name = CharField(max_length=100, help_text='Наименование категории')

#     def __str__(self) -> str:
#         return self.name


# class EventTypes(BaseModel):
#     name = CharField(max_length=100, help_text='Наименование типа мероприятия')

#     def __str__(self) -> str:
#         return self.name


# class Event(BaseModel):
#     category = ForeignKeyField(
#         Categories,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Категория'
#     )
#     date = DateField(help_text='Дата проведения')
#     describe = TextField(help_text='Описание')
#     event_type = ForeignKeyField(
#         EventTypes,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Тип мероприятия'
#     )

#     def validate(obj, create=False, id_=None):
#         if create:
#             if (
#                 obj['date'] < (
#                     datetime.date(datetime.today()) - timedelta(days=1)
#                 )
#             ):
#                 raise ValidationError('Выбранная дата уже прошла!')

#         return obj

#     def __str__(self) -> str:
#         return self.describe


# class WorkType(BaseModel):
#     name = CharField(max_length=100, help_text='Наименование вида работы')

#     def __str__(self) -> str:
#         return self.name


# class TasksStatuses(BaseModel):
#     status_name = CharField(max_length=100, help_text='Нименование статуса')

#     def __str__(self) -> str:
#         return self.status_name


# class Task(BaseModel):
#     date_registration = DateField(
#         help_text='Дата регистрации'
#     )
#     price = IntegerField(default=0)
#     event = ForeignKeyField(
#         Event,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Мероприятие'
#     )
#     work_type = ForeignKeyField(
#         WorkType,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Вид работы'
#     )
#     place = ForeignKeyField(
#         Place,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Помещение'
#     )
#     deadline = DateField(help_text='Дедлайн')

#     describe = TextField(help_text='Описание')
#     status = ForeignKeyField(
#         TasksStatuses,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Статус',
#     )
#     time_field = TimeField(help_text="Test time field")
#     date_time_field = DateTimeField(help_text="Test date time field")

#     def validate(obj, create=False, id_=None):
#         if obj['date_registration'] > obj['deadline']:
#             raise ValidationError(
#                 'Срок должен быть позже даты создания.'
#             )

#         return obj

#     def __str__(self) -> str:
#         return f"Task at {self.date_registration}"


# class Booking(BaseModel):
#     date_creation = DateTimeField(
#         default=datetime.now,
#         help_text='Дата создания'
#     )
#     event = ForeignKeyField(
#         Event,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Мероприятие'
#     )
#     start_booking_time = DateTimeField(help_text='Начало бронирования')
#     end_booking_time = DateTimeField(help_text='Окончание бронирования')

#     # todo filter by queryset
#     place = ForeignKeyField(
#         Place,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Помещение'
#     )
#     book_full = BooleanField(
#         help_text=(
#             'Забронировать все помещение'
#             '(если помещение может вместить только одно мероприятие, '
#             'то значение будет установлено автоматически)'
#         ),
#     )
#     comment = TextField(help_text='Комментарий')

#     def validate(obj, create=False, id_=None):
#         if not Place.get_by_id(obj['place']).big:
#             obj['book_full'] = False

#         if obj['start_booking_time'] >= obj['end_booking_time']:
#             raise ValidationError(
#                 'Начало бронирование должно быть раньше его конца.'
#             )

#         if create:
#             if obj['start_booking_time'] < datetime.today():
#                 raise ValidationError(
#                     'Указанная начальная дата и время бронирования уже прошла.'
#                 )

#         # todo make normal algorithm
#         filters = [
#             Booking.place == obj['place'],
#             Booking.start_booking_time <= obj['end_booking_time'],
#             Booking.end_booking_time >= obj['start_booking_time'],
#         ]
#         if id_:
#             filters.append(Booking.id != id_)

#         bookings = Booking.select().where(
#             *filters
#         )

#         if bookings.count() and not Place.get_by_id(obj['place']).big:
#             raise ValidationError(
#                 'Помещение уже полностью забронировано на это время'
#             )

#         segments = []
#         for segment in bookings:
#             segments.append((
#                 segment.start_booking_time,
#                 segment.end_booking_time
#             ))
#         if not segments_do_not_intersect(segments):
#             raise ValidationError(
#                 'Помещение было полностью забронировано на это время'
#             )

#         # if bookings.count() == 1:
#         #     if bookings[0].book_full
#         # or not Place.get_by_id(obj['place']).big:
#         #         raise ValidationError(
#         #             'Помещение было полностью забронировано на это время'
#         #         )

#         #     if obj['book_full']:
#         #         raise ValidationError(
#         #             'Невозможно забронировать полностью - '
#         #             'помещение уже частично забронировано.'
#         #         )

#         return obj

#     def __str__(self) -> str:
#         return f"Booking at {self.date_creation}"


# class ClubType(BaseModel):
#     name = CharField(max_length=100, help_text='Наименование вида кружка')

#     def __str__(self) -> str:
#         return self.name


# class Club(BaseModel):
#     name = CharField(max_length=100, help_text='Наименование кружка')
#     teacher = ForeignKeyField(
#         Teacher,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Преподаватель'
#     )
#     club_type = ForeignKeyField(
#         ClubType,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Вид кружка'
#     )
#     place = ForeignKeyField(
#         Place,
#         to_field='id',
#         on_delete='CASCADE',
#         help_text='Помещение'
#     )
#     date_start_working = DateField(help_text='Дата начала работы кружка')
#     working_days = DaysField(help_text='Дни занятий')
#     start_lesson_time = TimeField(help_text='Время начала занятия')
#     end_lesson_time = TimeField(help_text='Время конца занятия')

#     def __str__(self) -> str:
#         return (
#             self.name
#             + ': '
#             + str(self.start_lesson_time)
#             + ' - '
#             + str(self.end_lesson_time)
#         )

#     def validate(obj, create=False, id_=None):
#         if obj['start_lesson_time'] >= obj['end_lesson_time']:
#             raise ValidationError(
#                 'Начало занятия должно быть раньше его конца'
#             )

#         return obj


tables = [
    Place,
    Studio,
    Exhibit,
    Teacher,
]


def rebuild():
    print("start rebuilding database...")
    try:
        db.connect()
    except Exception:
        pass
    db.drop_tables(tables)
    db.create_tables(tables)
    print("success rebuild database")


def make():
    rebuild()
    print("Load base data...")
    from generators import generate
    generate()
    print("Load base data: success")


def manage_db():
    if not os.path.exists('./db.db'):
        make()

    if "--rebuild" in sys.argv:
        rebuild()
    if "--make" in sys.argv:
        make()


if __name__ == '__main__':
    manage_db()
