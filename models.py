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


db = SqliteDatabase(settings.DB_NAME, pragmas={'cache_size': 0})


class BaseModel(Model):
    class Meta:
        database = db


class Place(BaseModel):
    name = CharField(max_length=100)
    x_coord = FloatField()
    y_coord = FloatField()

    def __str__(self) -> str:
        return self.name


class Person(BaseModel):
    name = CharField()
    phone = CharField()
    age = IntegerField()
    male = CharField()
    place = ForeignKeyField(Place)

    def validate(self):
        ...

    def __str__(self) -> str:
        return str(self.name + ' ' + self.phone)


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
    tables = [Person, Place]

    db.connect()
    db.drop_tables(tables)
    db.create_tables(tables)

    # p, _ = Place.get_or_create(name='city', x_coord=1.15, y_coord=1.15)
    # User, _ = Person.get_or_create(
    # name='username', age=12, phone='123', male='1234', place=p)
    # User.name='hello'
    # print(User)
