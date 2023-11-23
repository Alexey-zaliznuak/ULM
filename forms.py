from flet import colors
from library.model_form import UIModelForm
from library.model_form.fields import ForeignKeyField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction,
    EditObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import (
    Categories,
    Place,
    EventTypes,
    Event,
    WorkType,
    TasksStatuses,
    Task,
)


class CategoriesForm(UIModelForm):
    class Meta:
        model = Categories
        fields = ('id', 'name',)
        objects_actions = (
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )

        table_actions = (CreateObjectAction, )


class PlaceForm(UIModelForm):
    category = ForeignKeyField('category', CategoriesForm, )

    class Meta:
        model = Place
        fields = ('id', 'name', 'category')
        objects_actions = (
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )

        table_actions = (CreateObjectAction, )


class EventTypesForm(UIModelForm):
    class Meta:
        model = EventTypes
        fields = ('id', 'name',)
        objects_actions = (
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )

        table_actions = (CreateObjectAction, )


class EventForm(UIModelForm):
    event_type = ForeignKeyField('event_type', EventTypesForm)
    category = ForeignKeyField('category', CategoriesForm, )

    class Meta:
        model = Event
        # todo create only fields
        fields = ('date', 'event_type', 'describe', 'category')
        objects_actions = (
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )

        table_actions = (CreateObjectAction, )


class WorkTypeForm(UIModelForm):
    class Meta:
        model = WorkType
        fields = ('id', 'name',)
        objects_actions = (
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )
        table_actions = (CreateObjectAction, )


class TasksForm(UIModelForm):
    event = ForeignKeyField('event', Event)
    work_type = ForeignKeyField('work_type', WorkType)
    place = ForeignKeyField('place', Place)
    status = ForeignKeyField('status', TasksStatuses)

    class Meta:
        model = Task
        # todo create only fields
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
            EditObjectAction,
            DetailObjectAction,
            DeleteObjectAction,
        )
        table_actions = (CreateObjectAction,)

    def get_row_params(self, obj, form, datatable) -> dict:
        colours = {
            TasksStatuses.get(
                TasksStatuses.status_name == 'Создано (черновик)'
            ): colors.WHITE,
            TasksStatuses.get(
                TasksStatuses.status_name == 'К выполнеию'
            ): colors.PINK_ACCENT_100,
            TasksStatuses.get(
                TasksStatuses.status_name == 'Выполнено'
            ): colors.GREEN_300,
        }
        return {
            'color': colours[obj.status]
        }
