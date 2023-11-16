from library.model_form import UIModelForm
from library.model_form.fields import ForeignKeyField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction,
    EditObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import PlaceCategories, Place, EventTypes, Event


class PlaceCategoriesForm(UIModelForm):
    class Meta:
        model = PlaceCategories
        fields = ('id', 'name',)
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )


class PlaceForm(UIModelForm):
    category = ForeignKeyField('category', PlaceCategoriesForm, )

    class Meta:
        model = Place
        fields = ('id', 'name', 'category')
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )


class EventTypesForm(UIModelForm):
    class Meta:
        model = EventTypes
        fields = ('id', 'name',)
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )


class EventForm(UIModelForm):
    event_type = ForeignKeyField('event_type', EventTypesForm)

    class Meta:
        model = Event
        fields = ('date', 'event_type', 'describe')
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )
