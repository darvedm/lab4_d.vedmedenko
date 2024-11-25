import csv
import random
from faker import Faker

# Ініціалізація Faker з українською локалізацією
fake = Faker('uk_UA')

# Словники для По батькові (по 50 варіантів кожен)
male_patronymics = [
    "Олександрович", "Іванович", "Сергійович", "Васильович", "Андрійович",
    "Петрович", "Михайлович", "Григорович", "Дмитрович", "Олегович",
    "Юрійович", "Богданович", "Володимирович", "Євгенович", "Романович",
    "Максимович", "Артемович", "Ігоревич", "Тарасович", "Степанович",
    "Леонідович", "Тимофійович", "Павлович", "Віталійович", "Олексійович",
    "Єгорович", "Антонович", "Валентинович", "Арсенович", "Маркелович",
    "Веніамінович", "Рустамович", "Святославович", "Ярославович", "Геннадійович",
    "Денисович", "Федорович", "Омелянович", "Назарович", "Борисович",
    "Георгійович", "Владиславович", "Костянтинович", "Ілліч", "Станіславович",
    "Захарович", "Аркадійович", "Матвійович", "Єфремович", "Лук’янович"
]

female_patronymics = [
    "Олександрівна", "Іванівна", "Сергіївна", "Василівна", "Андріївна",
    "Петрівна", "Михайлівна", "Григорівна", "Дмитрівна", "Олегівна",
    "Юріївна", "Богданівна", "Володимирівна", "Євгенівна", "Романівна",
    "Максимівна", "Артемівна", "Ігорівна", "Тарасівна", "Степанівна",
    "Леонідівна", "Тимофіївна", "Павлівна", "Віталіївна", "Олексіївна",
    "Єгорівна", "Антонівна", "Валентинівна", "Арсенівна", "Маркелівна",
    "Веніамінівна", "Рустамівна", "Святославівна", "Ярославівна", "Геннадіївна",
    "Денисівна", "Федорівна", "Омелянівна", "Назарівна", "Борисівна",
    "Георгіївна", "Владиславівна", "Костянтинівна", "Іллівна", "Станіславівна",
    "Захарівна", "Аркадіївна", "Матвіївна", "Єфремівна", "Лук’янівна"
]


# Функція для генерації запису
def generate_person(gender):
    if gender == "Чоловіча":
        first_name = fake.first_name_male()
        patronymic = random.choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        patronymic = random.choice(female_patronymics)

    last_name = fake.last_name()
    birth_date = fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%d-%m-%Y')
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone = fake.phone_number()
    email = fake.email()

    return [
        last_name, first_name, patronymic, gender, birth_date,
        position, city, address, phone, email
    ]


# Генерація записів
def generate_records(filename, num_records=2000):
    records = []
    for _ in range(int(num_records * 0.6)):  # Чоловіки (60%)
        records.append(generate_person("Чоловіча"))
    for _ in range(int(num_records * 0.4)):  # Жінки (40%)
        records.append(generate_person("Жіноча"))

    random.shuffle(records)  # Перемішати записи

    # Збереження у CSV файл
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([
            "Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
            "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"
        ])
        writer.writerows(records)


# Виклик функції для генерації CSV
generate_records('employees.csv')
print("Файл 'employees.csv' успішно створено!")
