from faker import Faker
import random
from my_autotests.data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()

def get_person():
    yield Person(
        full_name = faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email = faker_ru.email(),
        current_address = faker_ru.address(),
        permanent_address = faker_ru.address()
    )