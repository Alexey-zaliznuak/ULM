from library.core.validators import ValueValidator
from library.model_form import UIModelForm
from library.model_form.fields import PhoneField, IntegerField, ForeignKeyField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction,
    EditObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import Categories, Place, EventTypes, Event


class CategoriesForm(UIModelForm):
    class Meta:
        model = Categories
        fields = ('id', 'name',)
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )


class PlaceForm(UIModelForm):
    category = ForeignKeyField('category', CategoriesForm, )
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
    category = ForeignKeyField('category', CategoriesForm, )

    class Meta:
        model = Event
        # todo create only fields
        fields = ('date', 'event_type', 'describe', 'category')
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )
