from datetime import date, timedelta
from library.utils.model_data_generator import ModelDataGenerator
from models import (
    Categories,
    Place,
    EventTypes,
    Event,
    WorkType,
    TasksStatuses,
    Task,
)


class CategoriesGenerator(ModelDataGenerator):
    class Meta:
        model = Categories
        fields = ('name',)


class PlaceGenerator(ModelDataGenerator):
    class Meta:
        model = Place
        fields = ('name', 'category')


class EventTypesGenerator(ModelDataGenerator):
    class Meta:
        model = EventTypes
        fields = ('name',)


class EventGenerator(ModelDataGenerator):
    class Meta:
        model = Event
        fields = ('date', 'event_type', 'describe', 'category')


class WorkTypeGenerator(ModelDataGenerator):
    class Meta:
        model = WorkType
        fields = ('name',)


class TasksStatusesGenerator(ModelDataGenerator):
    class Meta:
        model = TasksStatuses
        fields = ('status_name',)


class TasksGenerator(ModelDataGenerator):
    class Meta:
        model = Task
        fields = (
            'date_registration',
            'event',
            'work_type',
            'place',
            'deadline',
            'describe',
            'status',
        )


def generate():
    CategoriesGenerator.generated_objects = [
        {'name': 'Развлекательное'},
        {'name': 'Просветительское'},
        {'name': 'Образовательное'},
    ]
    CategoriesGenerator.save()

    PlaceGenerator.generated_objects = [
        {
            'name': 'Музей № 1',
            'category': Categories.get(name='Просветительское')
        },
        {
            'name': 'Музей № 2',
            'category': Categories.get(name='Просветительское')
        },
        {
            'name': 'Татр № 1',
            'category': Categories.get(name='Развлекательное')
        },
        {
            'name': 'Секция Пения № 1',
            'category': Categories.get(name='Образовательное')
        },
    ]
    PlaceGenerator.save()

    EventTypesGenerator.generated_objects = [
        {'name': 'Спектакль'},
        {'name': 'Концерт'},
        {'name': 'Репетиция'},
        {'name': 'Выставка'},
    ]
    EventTypesGenerator.save()

    EventGenerator.generated_objects = [
        {
            'date': date.today() + timedelta(days=2),
            'event_type': EventTypes.get(name='Спектакль'),
            'describe': (
                'Театральное зрелище, представление, '
                'произведение театрального, сценического искусства',
            ),
            'category': Categories.get(name='Развлекательное')
        },
        {
            'date': date.today() + timedelta(days=3),
            'event_type': EventTypes.get(name='Концерт'),
            'describe': 'Концерт жизни', 'category': Categories.get(
                name='Просветительское'
            )
        },
        {
            'date': date.today() + timedelta(days=7),
            'event_type': EventTypes.get(name='Спектакль'),
            'describe': 'Образовательный концерт', 'category': Categories.get(
                name='Образовательное'
            )
        },
    ]
    EventGenerator.save()

    WorkTypeGenerator.generated_objects = [
        {'name': 'Принести стулья'},
        {'name': 'Принести плокаты'},
        {'name': 'Помыть полы'},
        {'name': 'Подгодовить помещение'},
    ]
    WorkTypeGenerator.save()

    TasksStatusesGenerator.generated_objects = [
        {'status_name': 'Создано (черновик)'},
        {'status_name': 'К выполнеию'},
        {'status_name': 'Выполнено'},
    ]
    TasksStatusesGenerator.save()

    TasksGenerator.generated_objects = [
        {
            'date-registration': date.today() - timedelta(days=4),
            'event': Event.get_by_id(1),
            'work_type': WorkType.get_by_id(1),
            'place': Place.get_by_id(1),
            'deadline': date.today() + timedelta(days=2),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(1)
        },
        {
            'date-registration': date.today() - timedelta(days=1),
            'event': Event.get_by_id(1),
            'work_type': WorkType.get_by_id(1),
            'place': Place.get_by_id(1),
            'deadline': date.today() + timedelta(days=12),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(1)
        },
        {
            'date-registration': date.today() - timedelta(days=2),
            'event': Event.get_by_id(2),
            'work_type': WorkType.get_by_id(2),
            'place': Place.get_by_id(2),
            'deadline': date.today() + timedelta(days=5),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(2)
        },
        {
            'date-registration': date.today() - timedelta(days=10),
            'event': Event.get_by_id(2),
            'work_type': WorkType.get_by_id(2),
            'place': Place.get_by_id(2),
            'deadline': date.today() + timedelta(days=25),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(2)
        },
        {
            'date-registration': date.today() - timedelta(days=6),
            'event': Event.get_by_id(3),
            'work_type': WorkType.get_by_id(3),
            'place': Place.get_by_id(3),
            'deadline': date.today() + timedelta(days=5),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(3)
        },
        {
            'date-registration': date.today() - timedelta(days=6),
            'event': Event.get_by_id(3),
            'work_type': WorkType.get_by_id(3),
            'place': Place.get_by_id(4),
            'deadline': date.today() + timedelta(days=4),
            'describe': 'Лучшая заявка в мире',
            'status': TasksStatuses.get_by_id(3)
        },
    ]
