from faker import Faker
import random
from data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


def get_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(1, 100),
        department=faker_ru.job(),
        salary=random.randint(100, 1000000)
    )


def generated_file():
    path = rf"../test{random.randint(0, 999)}.txt"
    with open(path, 'w+') as f:
        f.write(f"""Hello World{random.randint(0, 999)}""")
        f.close()
    return f.name, path
