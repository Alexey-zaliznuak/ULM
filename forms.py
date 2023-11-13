from library.core.validators import ValueValidator
from library.model_form import UIModelForm
from library.model_form.fields import PhoneField, IntegerField, ForeignKeyField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction,
    EditObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import Place, Person


class PlaceForm(UIModelForm):
    class Meta:
        model = Place
        fields = ('id', 'name', 'x_coord', 'y_coord')
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )


class PersonUIModelForm(UIModelForm):
    phone = PhoneField('phone')
    age = IntegerField(
        'age',
        required=True,
        validators=[ValueValidator(3, 124)]
    )
    place = ForeignKeyField('place', PlaceForm)

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'phone',
            'age',
            'male',
            'place',
        )
        objects_actions = (
            DeleteObjectAction,
            DetailObjectAction,
            EditObjectAction
        )
        table_actions = (CreateObjectAction, )
