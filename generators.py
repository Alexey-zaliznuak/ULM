from library.utils.model_data_generator import ModelDataGenerator
from library.utils.model_data_generator.generators import (
    BooleanGenerator,
    ForeignKeyGenerator,
    NameGenerator,
    PhoneNumberGenerator,
    PositiveIntegerGenerator,
)

from models import Person, GodModel


class PersonModelDataGenerator(ModelDataGenerator):
    age = PositiveIntegerGenerator(mx=100)
    name = NameGenerator()
    phone = PhoneNumberGenerator()
    male = BooleanGenerator()

    class Meta:
        model = Person
        fields = (
            'age',
            'male',
            'name',
            'phone',
        )


class GodModelDataGenerator(ModelDataGenerator):
    name = NameGenerator()
    years = PositiveIntegerGenerator()
    entity = ForeignKeyGenerator(Person)

    class Meta:
        model = GodModel
        fields = (
            'entity',
            'is_god',
            'name',
            'years',
            'date_birth',
            'date_time_birth',
            'divine_value',
            'divine_description',
            'replenish_divine_time',
            'divine_uuid',
        )


if __name__ == "__main__":
    PersonModelDataGenerator.generate_rows(15)
    PersonModelDataGenerator.save()

    GodModelDataGenerator.generate_rows(10)
    GodModelDataGenerator.save()
