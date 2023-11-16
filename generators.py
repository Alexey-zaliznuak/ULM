from datetime import date, timedelta
from library.utils.model_data_generator import ModelDataGenerator
from models import PlaceCategories, Place, EventTypes, Event


class PlaceCategoriesGenerator(ModelDataGenerator):
    class Meta:
        model=PlaceCategories
        fields=('name',)

PlaceCategoriesGenerator.generated_objects = [
    {'name': 'Развлекательное'},
    {'name': 'Просветительское'},
    {'name': 'Образовательное'},
]
PlaceCategoriesGenerator.save()


class PlaceGenerator(ModelDataGenerator):
    class Meta:
        model=Place
        fields=('name', 'category')

PlaceGenerator.generated_objects = [
    {'name': 'Музей № 1', 'category': PlaceCategories.get(name='Просветительское')},
    {'name': 'Музей № 2', 'category': PlaceCategories.get(name='Просветительское')},
    {'name': 'Татр № 1', 'category': PlaceCategories.get(name='Развлекательное')},
    {'name': 'Секция Пения № 1', 'category': PlaceCategories.get(name='Образовательное')},
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
        fields=('date', 'event_type', 'describe')

EventGenerator.generated_objects = [
    {'date': date.today()+timedelta(days=2), 'event_type': EventTypes.get(name='Спектакль'), 'describe': 'Super event1'},
    {'date': date.today()+timedelta(days=3), 'event_type': EventTypes.get(name='Концерт'), 'describe': 'Super event1'},
    {'date': date.today()+timedelta(days=7), 'event_type': EventTypes.get(name='Спектакль'), 'describe': 'Super event1'},
]
EventGenerator.save()
