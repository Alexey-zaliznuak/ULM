from datetime import date, datetime, timedelta, time
from peewee import Model, Field
from library.utils.model_data_generator import ModelDataGenerator
from models import (
    Place,
    Studio,
    Exhibit,
    Teacher,
)


# class CategoriesGenerator(ModelDataGenerator):
#     class Meta:
#         model = Categories
#         fields = ('name',)


class PlacesGenerator(ModelDataGenerator):
    class Meta:
        model = Place
        fields = ('name', 'capacity', 'describe')


class StudiosGenerator(ModelDataGenerator):
    class Meta:
        model = Studio
        fields = ('name', 'describe')


class ExhibitsGenerator(ModelDataGenerator):
    class Meta:
        model = Exhibit
        fields = ('name', 'describe')


class TeachersGenerator(ModelDataGenerator):
    class Meta:
        model = Teacher
        fields = ('full_name',)


# class EventTypesGenerator(ModelDataGenerator):
#     class Meta:
#         model = EventTypes
#         fields = ('name',)


# class EventGenerator(ModelDataGenerator):
#     class Meta:
#         model = Event
#         fields = ('date', 'event_type', 'describe', 'category')


# class WorkTypeGenerator(ModelDataGenerator):
#     class Meta:
#         model = WorkType
#         fields = ('name',)


# class TasksStatusesGenerator(ModelDataGenerator):
#     class Meta:
#         model = TasksStatuses
#         fields = ('status_name',)


# class BookingGenerator(ModelDataGenerator):
#     class Meta:
#         model = Booking
#         fields = (
#             'place',
#             'book_full',
#             'event',
#             'start_booking_time',
#             'end_booking_time',
#             'comment',
#             'date_creation',
#         )


# class TasksGenerator(ModelDataGenerator):
#     class Meta:
#         model = Task
#         fields = (
#             'date_registration',
#             'event',
#             'work_type',
#             'place',
#             'deadline',
#             'describe',
#             'status',
#         )


# class ClubTypesGenerator(ModelDataGenerator):
#     class Meta:
#         model = ClubType
#         fields = ('name',)


# class ClubsGenerators(ModelDataGenerator):
#     class Meta:
#         model = Club
#         fields = (
#             'name',
#             'tacher',
#             'club_type',
#             'place',
#             'date_start_working',
#             'working_days',
#             'start_lesson_time',
#             'start_lesson_time',
#         )

# fks:
# {
        # field_name: (FKModel, FKField)
#}


def load_excel(f_name, rows:list[str], floats=[], fk_s = {}) -> list[dict[str, str]]:
    # input()
    import xlrd
    workbook = xlrd.open_workbook(f"{f_name}.xls")
    queryset = []
    # Open the worksheet
    worksheet = workbook.sheet_by_index(0)

    # Iterate the rows and columns
    for i in range(1, 10**5):
        try:
            worksheet.cell_value(i, 0)
            # print("blyat")
        except IndexError:
            return queryset

        new = {}
        for j in range(0, 10**5):
            # Print the cell values with tab space
            try:
                cell = worksheet.cell_value(i, j)
                if rows[j] not in floats and isinstance(cell, float):
                    new[rows[j]] = int(cell)
                
                elif rows[j] in fk_s.keys():
                    param = fk_s[rows[j]]
                    model, field = param
                    cell = model.select().where(field==cell).execute()[0]
                    # input()
                    new[rows[j]] = cell.id

                else:
                    new[rows[j]] = cell

            except IndexError:
                break
        queryset.append(new)
    # print(queryset)
    return queryset

def generate_places():
    PlacesGenerator.generated_objects = load_excel("Spaces", ["name", "capacity", "describe",])
    PlacesGenerator.save()
 
def generate_studios():
    StudiosGenerator.generated_objects = load_excel("Studios", ["name", "describe",])
    StudiosGenerator.save()
 
def generate_exhibits():
    ExhibitsGenerator.generated_objects = load_excel("Exhibits", ["name", "studio"], fk_s={'studio': (Studio, Studio.name)})
    ExhibitsGenerator.save()
 
def generate_teachers():
    TeachersGenerator.generated_objects = load_excel("teachers", ["full_name"])
    TeachersGenerator.save()
 
 
def generate():
    generate_places()
    StudiosGenerator.generated_objects = [{'name': "Культурный центр", "describe": "Весь культурный центр в целом"}]
    StudiosGenerator.save()
    generate_teachers()
    generate_studios()
    generate_exhibits()

def smth():
    pass
    # CategoriesGenerator.generated_objects = [
    #     {'name': 'Развлекательное'},
    #     {'name': 'Просветительское'},
    #     {'name': 'Образовательное'},
    # ]
    # CategoriesGenerator.save()

    # PlaceGenerator.generated_objects = [
    #     {
    #         'name': 'Музей № 1',
    #         'category': Categories.get(name='Просветительское'),
    #     },
    #     {
    #         'name': 'Музей № 2',
    #         'category': Categories.get(name='Просветительское'),
    #     },
    #     {
    #         'name': 'Татр № 1',
    #         'category': Categories.get(name='Развлекательное'),
    #         'big': True
    #     },
    #     {
    #         'name': 'Секция Пения № 1',
    #         'category': Categories.get(name='Образовательное'),
    #         'big': True
    #     },

    #     # for clubs
    #     {
    #         'name': 'Секция Пения № 2',  # пение
    #         'category': Categories.get(name='Образовательное'),
    #     },
    #     {
    #         'name': 'Секция Пения № 3',  # гитара
    #         'category': Categories.get(name='Образовательное'),
    #     },
    #     {
    #         'name': 'Зал Звездной ночи',  # рисование
    #         'category': Categories.get(name='Образовательное'),
    #     },
    #     {
    #         'name': 'Помещение 0-08',  # шахматы
    #         'category': Categories.get(name='Образовательное'),
    #     },
    # ]
    # PlaceGenerator.save()

    # EventTypesGenerator.generated_objects = [
    #     {'name': 'Спектакль'},
    #     {'name': 'Концерт'},
    #     {'name': 'Репетиция'},
    #     {'name': 'Выставка'},
    # ]
    # EventTypesGenerator.save()

    # EventGenerator.generated_objects = [
    #     {
    #         'date': date.today() + timedelta(days=2),
    #         'event_type': EventTypes.get(name='Спектакль'),
    #         'describe': (
    #             'Театральное зрелище'
    #         ),
    #         'category': Categories.get(name='Развлекательное')
    #     },
    #     {
    #         'date': date.today() + timedelta(days=3),
    #         'event_type': EventTypes.get(name='Концерт'),
    #         'describe': 'Концерт жизни', 'category': Categories.get(
    #             name='Просветительское'
    #         )
    #     },
    #     {
    #         'date': date.today() + timedelta(days=7),
    #         'event_type': EventTypes.get(name='Спектакль'),
    #         'describe': 'Образовательный концерт', 'category': Categories.get(
    #             name='Образовательное'
    #         )
    #     },
    # ]
    # EventGenerator.save()

    # WorkTypeGenerator.generated_objects = [
    #     {'name': 'Принести стулья'},
    #     {'name': 'Принести плакаты'},
    #     {'name': 'Помыть полы'},
    #     {'name': 'Подготовить помещение'},
    # ]
    # WorkTypeGenerator.save()

    # TasksStatusesGenerator.generated_objects = [
    #     {'status_name': 'Создано (черновик)'},
    #     {'status_name': 'К выполнению'},
    #     {'status_name': 'Выполнено'},
    # ]
    # TasksStatusesGenerator.save()

    # TasksGenerator.generated_objects = [
    #     {
    #         'date_registration': date.today() - timedelta(days=4),
    #         'event': Event.get_by_id(1),
    #         'work_type': WorkType.get_by_id(1),
    #         'place': Place.get_by_id(1),
    #         'deadline': date.today() + timedelta(days=2),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(1),
    #         'time_field': time(10, 10),
    #         'date_time_field': datetime.now() + timedelta(days=10)
    #     },
    #     {
    #         'date_registration': date.today() - timedelta(days=1),
    #         'event': Event.get_by_id(1),
    #         'work_type': WorkType.get_by_id(1),
    #         'place': Place.get_by_id(1),
    #         'deadline': date.today() + timedelta(days=12),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(1),
    #         'time_field': time(20, 30),
    #         'date_time_field': datetime.now() + timedelta(days=-10)
    #     },
    #     {
    #         'date_registration': date.today() - timedelta(days=2),
    #         'event': Event.get_by_id(2),
    #         'work_type': WorkType.get_by_id(2),
    #         'place': Place.get_by_id(2),
    #         'deadline': date.today() + timedelta(days=5),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(2),
    #         'time_field': time(10, 00),
    #         'date_time_field': datetime.now() + timedelta(days=100)
    #     },
    #     {
    #         'date_registration': date.today() - timedelta(days=10),
    #         'event': Event.get_by_id(2),
    #         'work_type': WorkType.get_by_id(2),
    #         'place': Place.get_by_id(2),
    #         'deadline': date.today() + timedelta(days=25),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(2),
    #         'time_field': time(0, 0),
    #         'date_time_field': datetime.now() + timedelta(days=0)
    #     },
    #     {
    #         'date_registration': date.today() - timedelta(days=6),
    #         'event': Event.get_by_id(3),
    #         'work_type': WorkType.get_by_id(3),
    #         'place': Place.get_by_id(3),
    #         'deadline': date.today() + timedelta(days=5),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(3),
    #         'time_field': time(0, 0),
    #         'date_time_field': datetime.now() + timedelta(days=3)
    #     },
    #     {
    #         'date_registration': date.today() - timedelta(days=6),
    #         'event': Event.get_by_id(3),
    #         'work_type': WorkType.get_by_id(3),
    #         'place': Place.get_by_id(4),
    #         'deadline': date.today() + timedelta(days=4),
    #         'describe': 'Лучшая заявка в мире',
    #         'status': TasksStatuses.get_by_id(3),
    #         'time_field': time(0, 0),
    #         'date_time_field': datetime.now() + timedelta(days=365 + 10)
    #     },
    # ]

    # TasksGenerator.save()

    # BookingGenerator.generated_objects = [
    #     {
    #         'place': Place.get_by_id(1),
    #         'book_full': False,
    #         'event': Event.get_by_id(1),
    #         'start_booking_time': datetime.now() + timedelta(hours=2),
    #         'end_booking_time': datetime.now() + timedelta(hours=4),
    #         'comment': 'Без комментариев',
    #         'date_creation': datetime.now() + timedelta(hours=1),
    #     },
    #     {
    #         'place': Place.get_by_id(4),
    #         'book_full': True,
    #         'event': Event.get_by_id(2),
    #         'start_booking_time': datetime.now() + timedelta(hours=5),
    #         'end_booking_time': datetime.now() + timedelta(hours=15),
    #         'comment': 'Без комментариев',
    #         'date_creation': datetime.now() + timedelta(hours=1),
    #     },
    #     {
    #         'place': Place.get_by_id(3),
    #         'book_full': False,
    #         'event': Event.get_by_id(3),
    #         'start_booking_time': datetime.now() + timedelta(hours=2),
    #         'end_booking_time': datetime.now() + timedelta(hours=7),
    #         'comment': 'Без комментариев',
    #         'date_creation': datetime.now() + timedelta(hours=1),
    #     },
    #     {
    #         'place': Place.get_by_id(3),
    #         'book_full': False,
    #         'event': Event.get_by_id(3),
    #         'start_booking_time': datetime.now() + timedelta(hours=5),
    #         'end_booking_time': datetime.now() + timedelta(hours=8),
    #         'comment': 'Без комментариев',
    #         'date_creation': datetime.now() + timedelta(hours=1),
    #     },
    # ]
    # BookingGenerator.save()

    # TeachersGenerator.generated_objects = [
    #     {'full_name': 'Луна Шарон Мариковна'},
    #     {'full_name': 'Митчел Леонард Клейнович'},
    #     {'full_name': 'Шейлина Анастасия Филиповна'},
    #     {'full_name': 'Логран Каземир Иоаннович'},
    # ]
    # TeachersGenerator.save()

    # ClubTypesGenerator.generated_objects = [
    #     {'name': 'Кружок пения'},
    #     {'name': 'Кружок игры на гитаре'},
    #     {'name': 'Кружок рисования'},
    #     {'name': 'Кружок шахмат'},
    # ]
    # ClubTypesGenerator.save()

    # ClubsGenerators.generated_objects = [
    #     {
    #         'name': 'Ангельн',
    #         'teacher': Teacher.get_by_id(1),
    #         'club_type': ClubType.get_by_id(1),
    #         'place': Place.get_by_id(5),
    #         'date_start_working': date.today() - timedelta(days=20),
    #         'working_days': '3:пн;ср;пт',
    #         'start_lesson_time': time(14, 30),
    #         'end_lesson_time': time(17)
    #     },
    #     {
    #         'name': 'Ночной хор',
    #         'teacher': Teacher.get_by_id(2),
    #         'club_type': ClubType.get_by_id(2),
    #         'place': Place.get_by_id(6),
    #         'date_start_working': date.today() - timedelta(days=120),
    #         'working_days': '2:пн;пт',
    #         'start_lesson_time': time(16, 30),
    #         'end_lesson_time': time(17, 30)
    #     },
    #     {
    #         'name': 'Звездное полотно',
    #         'teacher': Teacher.get_by_id(3),
    #         'club_type': ClubType.get_by_id(3),
    #         'place': Place.get_by_id(7),
    #         'date_start_working': date.today() - timedelta(days=10),
    #         'working_days': '3:вт;чт;сб',
    #         'start_lesson_time': time(11),
    #         'end_lesson_time': time(13, 15)
    #     },
    #     {
    #         'name': 'Дебют',
    #         'teacher': Teacher.get_by_id(4),
    #         'club_type': ClubType.get_by_id(4),
    #         'place': Place.get_by_id(8),
    #         'date_start_working': date.today() - timedelta(days=300),
    #         'working_days': '2:пн;вс',
    #         'start_lesson_time': time(18, 30),
    #         'end_lesson_time': time(20)
    #     }
    # ]
    # ClubsGenerators.save()


# print(load_excel("Spaces", ["Наменование", "Вместимость", "Описание",]))
