import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Функція для обчислення віку
def calculate_age(birth_date):
    """Розрахунок віку на основі дати народження."""
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def analyze_csv(csv_path):
    """Аналіз CSV-файлу."""
    try:
        if not os.path.exists(csv_path):
            print("Файл CSV не знайдено!")
            return

        # Зчитування даних
        data = pd.read_csv(csv_path)
        print("Ok, файл CSV успішно зчитано.")

        # Додавання вікової категорії
        data['Вік'] = data['Дата народження'].apply(calculate_age)
        data['Категорія'] = pd.cut(
            data['Вік'],
            bins=[0, 18, 45, 70, float('inf')],
            labels=["younger_18", "18-45", "45-70", "older_70"]
        )

        # Кількість співробітників за статтю
        gender_count = data['Стать'].value_counts()
        print("\nКількість співробітників за статтю:")
        print(gender_count)

        # Побудова діаграми за статтю
        plt.figure(figsize=(8, 5))
        gender_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'])
        plt.title("Кількість співробітників за статтю")
        plt.ylabel('')
        plt.savefig("gender_distribution.png")
        plt.show()

        # Кількість співробітників за віковими категоріями
        age_category_count = data['Категорія'].value_counts()
        print("\nКількість співробітників за віковими категоріями:")
        print(age_category_count)

        # Побудова діаграми за віковими категоріями
        plt.figure(figsize=(8, 5))
        age_category_count.plot(kind='bar', color='skyblue')
        plt.title("Кількість співробітників за віковими категоріями")
        plt.xlabel("Категорії")
        plt.ylabel("Кількість")
        plt.xticks(rotation=0)
        plt.savefig("age_category_distribution.png")
        plt.show()

        # Кількість співробітників за статтю і віковими категоріями
        gender_age_category_count = data.groupby(['Категорія', 'Стать'], observed=False).size().unstack(fill_value=0)
        print("\nКількість співробітників за статтю і віковими категоріями:")
        print(gender_age_category_count)

        # Побудова діаграм за статтю і віковими категоріями
        gender_age_category_count.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightblue', 'pink'])
        plt.title("Кількість співробітників за статтю і віковими категоріями")
        plt.xlabel("Категорії")
        plt.ylabel("Кількість")
        plt.xticks(rotation=0)
        plt.legend(title="Стать")
        plt.savefig("gender_age_category_distribution.png")
        plt.show()

    except Exception as e:
        print("Помилка при обробці CSV файлу:", str(e))


csv_file_path = "employees.csv"
analyze_csv(csv_file_path)
