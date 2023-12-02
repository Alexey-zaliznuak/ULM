from flet import colors, icons
from library.model_form import UIModelForm
from library.model_form.fields import ForeignKeyField
from library.model_form.actions.objects import (
    CreateForeignObjectAction,
    DeleteObjectAction,
    DetailObjectAction,
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
)


RUDActions = [
    EditObjectAction(),
    DetailObjectAction(),
    DeleteObjectAction(),
]


class CategoriesForm(UIModelForm):
    class Meta:
        model = Categories
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


class PlaceForm(UIModelForm):
    category = ForeignKeyField('category', CategoriesForm, )

    class Meta:
        model = Place
        fields = ('id', 'name', 'category', 'big')
        objects_actions = RUDActions

        table_actions = (CreateObjectAction, )


class EventTypesForm(UIModelForm):
    class Meta:
        model = EventTypes
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


class EventForm(UIModelForm):
    event_type = ForeignKeyField('event_type', EventTypesForm)
    category = ForeignKeyField('category', CategoriesForm, )

    class Meta:
        model = Event
        # todo create only fields
        fields = ('date', 'event_type', 'describe', 'category')
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


class WorkTypeForm(UIModelForm):
    class Meta:
        model = WorkType
        fields = ('id', 'name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


class TasksStatusesForm(UIModelForm):
    class Meta:
        model = TasksStatuses
        fields = ('id', 'status_name',)
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


class TasksForm(UIModelForm):
    event = ForeignKeyField('event', EventForm)
    work_type = ForeignKeyField('work_type', WorkTypeForm)
    place = ForeignKeyField('place', PlaceForm)
    status = ForeignKeyField('status', TasksStatusesForm)

    class Meta:
        model = Task
        fields = (
            'date_registration',
            'event',
            'work_type',
            'place',
            'deadline',
            'describe',
            'status',
        )
        objects_actions = (
            *RUDActions,
            SetValueObjectAction(
                Task.status, TasksStatuses.get(status_name='Выполнено')
            )
        )
        table_actions = (CreateObjectAction,)

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
    place = ForeignKeyField('place', PlaceForm)
    event = ForeignKeyField('event', EventForm)

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
        objects_actions = RUDActions
        table_actions = (CreateObjectAction, )


EventForm.Meta.objects_actions = [
    *EventForm.Meta.objects_actions,
    CreateForeignObjectAction(
        BookingForm(),
        Booking.event,
        icon=icons.FACT_CHECK_OUTLINED
    )
]
