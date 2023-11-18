from datetime import date, timedelta
from library.utils.model_data_generator import ModelDataGenerator
from models import Categories, Place, EventTypes, Event


class CategoriesGenerator(ModelDataGenerator):
    class Meta:
        model = Categories
        fields = ('name',)

CategoriesGenerator.generated_objects = [
    {'name': 'Развлекательное'},
    {'name': 'Просветительское'},
    {'name': 'Образовательное'},
]
CategoriesGenerator.save()


class PlaceGenerator(ModelDataGenerator):
    class Meta:
        model = Place
        fields = ('name', 'category')


PlaceGenerator.generated_objects = [
    {'name': 'Музей № 1', 'category': Categories.get(name='Просветительское')},
    {'name': 'Музей № 2', 'category': Categories.get(name='Просветительское')},
    {'name': 'Татр № 1', 'category': Categories.get(name='Развлекательное')},
    {'name': 'Секция Пения № 1', 'category': Categories.get(name='Образовательное')},
]
PlaceGenerator.save()


class EventTypesGenerator(ModelDataGenerator):
    class Meta:
        model=EventTypes
        fields=('name',)

EventTypesGenerator.generated_objects = [
    {'name': 'Спектакль'},
    {'name': 'Концерт'},
    {'name': 'Репетиция'},
    {'name': 'Выставка'},
]
EventTypesGenerator.save()


class EventGenerator(ModelDataGenerator):
    class Meta:
        model=Event
        fields=('date', 'event_type', 'describe', 'category')

EventGenerator.generated_objects = [
    {'date': date.today()+timedelta(days=2), 'event_type': EventTypes.get(name='Спектакль'), 'describe': 'Super event1', 'category': Categories.get(name='Развлекательное')},
    {'date': date.today()+timedelta(days=3), 'event_type': EventTypes.get(name='Концерт'), 'describe': 'Super event1', 'category': Categories.get(name='Просветительское')},
    {'date': date.today()+timedelta(days=7), 'event_type': EventTypes.get(name='Спектакль'), 'describe': 'Super event1', 'category': Categories.get(name='Образовательное')},
]
EventGenerator.save()
