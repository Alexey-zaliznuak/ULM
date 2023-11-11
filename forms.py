from library.core.validators import ValueValidator
from library.model_form import UIModelForm
from library.model_form.fields import PhoneField, IntegerField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction,
    EditObjectAction,
)
from library.model_form.actions.table import CreateObjectAction

from models import Person


class PersonUIModelForm(UIModelForm):
    phone = PhoneField('phone')
    age = IntegerField(
        'age',
        required=True,
        validators=[ValueValidator(3, 124)]
    )

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'phone',
            'age',
            'male',
        )
        objects_actions = (DeleteObjectAction, DetailObjectAction, EditObjectAction)
        table_actions = (CreateObjectAction, )
