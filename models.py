from peewee import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    FloatField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
    TimeField,
    UUIDField
)

import settings

from library.core.exceptions import ValidationError

db = SqliteDatabase(settings.DB_NAME, pragmas={'cache_size': 0})


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    phone = CharField()
    age = IntegerField()
    male = BooleanField()

    def validate(self):
        if not (1 < int(self.age) < 120):
            raise ValidationError('uncorrect age - ' + str(self.age))


class GodModel(BaseModel):
    entity = ForeignKeyField(Person, 'id')
    is_god = BooleanField()
    name = CharField(max_length=150)
    years = IntegerField()
    date_birth = DateField()
    date_time_birth = DateTimeField()
    divine_value = FloatField()
    divine_description = TextField()
    replenish_divine_time = TimeField()
    divine_uuid = UUIDField()


if __name__ == '__main__':
    tables = [Person, GodModel]

    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)
