from library.model_form import UIModelForm
from library.model_form.ui_fields import PhoneField
from library.model_form.actions.objects import (
    DeleteObjectAction,
    DetailObjectAction
)
from library.model_form.actions.table import CreateObjectAction

from models import Person


class PersonUIModelForm(UIModelForm):
    phone = PhoneField('phone')

    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'phone',
            'age',
            'male',
        )
        objects_actions = (DeleteObjectAction, DetailObjectAction)
        table_actions = (CreateObjectAction, )
