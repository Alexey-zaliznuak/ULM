from flet import colors, icons
from library.model_form import UIModelForm
from library.model_form.fields import ForeignKeyField, BooleanField
from library.model_form.actions.objects import (
    CreateForeignObjectAction,
    DeleteObjectAction,
    DataTableDetailObjectAction,
    EditObjectAction,
    SetValueObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import (
    Booking,
    Categories,
    Place,
    EventTypes,
    Event,
    WorkType,
    TasksStatuses,
    Task,
    Teacher,
    ClubType,
    Club,
)


RUDActions = [
    EditObjectAction(),
    DataTableDetailObjectAction(),
    DeleteObjectAction(),
]


# TODO use model title with datatable column name


class CategoriesForm(UIModelForm):
    class Meta:
        model = Categories
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Категории'


class PlaceForm(UIModelForm):
    category = ForeignKeyField(
        'category',
        CategoriesForm, datatable_column_title='Категория'
    )
    big = BooleanField(
        'big',
        datatable_column_title='Вмещает 2 мероприятия',
    )

    class Meta:
        model = Place
        fields = ('id', 'name', 'category', 'big')
        objects_actions = RUDActions

        table_actions = (CreateObjectAction, )
        model_title = 'Пространства'


class EventTypesForm(UIModelForm):
    class Meta:
        model = EventTypes
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Вид мероприятия'


class EventForm(UIModelForm):
    event_type = ForeignKeyField(
        'event_type',
        EventTypesForm, datatable_column_title='Вид мероприятия'
    )
    category = ForeignKeyField(
        'category',
        CategoriesForm, datatable_column_title='Категория'
    )

    class Meta:
        model = Event
        # todo create only fields
        fields = ('date', 'event_type', 'describe', 'category')
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Мероприятие'


class WorkTypeForm(UIModelForm):
    class Meta:
        model = WorkType
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Вид работы'


class TasksStatusesForm(UIModelForm):
    class Meta:
        model = TasksStatuses
        fields = ('id', 'status_name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Статус заявки'


class TasksForm(UIModelForm):
    event = ForeignKeyField(
        'event',
        EventForm, datatable_column_title='События'
    )
    work_type = ForeignKeyField(
        'work_type',
        WorkTypeForm, datatable_column_title='Вид работы'
    )
    place = ForeignKeyField(
        'place',
        PlaceForm, datatable_column_title='Помещение'
    )
    status = ForeignKeyField(
        'status',
        TasksStatusesForm, datatable_column_title='Статус'
    )

    class Meta:
        model = Task
        fields = (
            'date_registration',
            'price',
            'event',
            'work_type',
            'place',
            'deadline',
            'describe',
            'status',
        )
        objects_actions = (
            *RUDActions,
            # SetValueObjectAction(
            #     Task.status, TasksStatuses.get(status_name='Выполнено')
            # )
        )
        table_actions = (CreateObjectAction,)
        model_title = 'Заявки'

    def get_row_params(self, obj, form, datatable) -> dict:
        colours = {
            TasksStatuses.get(
                TasksStatuses.status_name == 'Создано (черновик)'
            ): colors.WHITE,
            TasksStatuses.get(
                TasksStatuses.status_name == 'К выполнению'
            ): colors.PINK_ACCENT_100,
            TasksStatuses.get(
                TasksStatuses.status_name == 'Выполнено'
            ): colors.GREY_300,
        }
        return {
            'color': colours[obj.status]
        }


class BookingForm(UIModelForm):
    # todo queryset
    place = ForeignKeyField(
        'place',
        PlaceForm, datatable_column_title='Помещение'
    )
    event = ForeignKeyField(
        'event',
        EventForm, datatable_column_title='Событие'
    )

    class Meta:
        model = Booking
        fields = (
            'place',
            'book_full',
            'event',
            'start_booking_time',
            'end_booking_time',
            'comment',
            'date_creation',
        )
        read_only_fields = ('date_creation', )
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Бронирование'


EventForm.Meta.objects_actions = [
    *EventForm.Meta.objects_actions,
    CreateForeignObjectAction(
        BookingForm(),
        Booking.event,
        icon=icons.FACT_CHECK_OUTLINED
    )
]


class TeacherForm(UIModelForm):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Преподаватель'


class ClubTypeForm(UIModelForm):
    class Meta:
        model = ClubType
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Вид кружка'


class ClubForm(UIModelForm):
    teacher = ForeignKeyField(
        'teacher',
        TeacherForm, datatable_column_title='Преподаватель'
    )
    club_type = ForeignKeyField(
        'club_type',
        ClubTypeForm, datatable_column_title='Вид кружка'
    )
    place = ForeignKeyField(
        'place',
        PlaceForm, datatable_column_title='Помещение'
    )

    class Meta:
        model = Club
        fields = (
            'name',
            'date_start_working',
            'club_type',
            'place',
            'working_days',
            'start_lesson_time',
            'end_lesson_time',
            'teacher',
        )
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )
        model_title = 'Кружок'
