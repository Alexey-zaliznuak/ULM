from library.model_form import UIModelForm
from library.model_form.actions.objects import DeleteObjectAction, DetailObjectAction

from models import Person


class PersonUIModelForm(UIModelForm):
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
