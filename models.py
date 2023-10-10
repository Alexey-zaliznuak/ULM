from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateField,
    TimeField,
    DateTimeField,
    IntegerField,
    ForeignKeyField,
)

import settings


db = SqliteDatabase(settings.DB_NAME, pragmas={'cache_size': 0})


class BaseModel(Model):
    class Meta:
        database = db


class Place(BaseModel):
    name = CharField()
    date_added = DateField()
    time_added = TimeField()
    dt_field = DateTimeField()


class Person(BaseModel):
    name = CharField()
    phone = CharField()
    age = IntegerField()


class Hotel(BaseModel):
    name = CharField(max_length=120)
    place = ForeignKeyField(Place, backref='hotels', related_name='hootels')
    bellboy = ForeignKeyField(Person)

    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':
    tables = [Person, Place, Hotel]

    db.connect()
    # db.drop_tables(tables)
    # db.create_tables(tables)
    p = Place.get(
        name='name',
        date_added='now',
        time_added='now',
        dt_field='now'
    )
    p.delete_instance()
