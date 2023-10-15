from library.utils.model_data_generator import ModelDataGenerator
from library.utils.model_data_generator.generators import (
    PositiveIntegerGenerator,
    PhoneNumberGenerator,
    NameGenerator,
)

from models import Person


class PersonModelDataGenerator(ModelDataGenerator):
    age = PositiveIntegerGenerator(mx=100)
    name = NameGenerator()
    phone = PhoneNumberGenerator()

    class Meta:
        model = Person
        fields = (
            'age',
            'male',
            'name',
            'phone',
        )


if __name__ == "__main__":
    PersonModelDataGenerator.generate_rows(100)
    PersonModelDataGenerator.save()
