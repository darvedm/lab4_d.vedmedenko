import pandas as pd
from datetime import datetime
import os

def calculate_age(birth_date):
    """Розрахунок віку на основі дати народження."""
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def process_csv_to_xlsx(csv_path, xlsx_path):
    try:
        # Перевірка існування CSV файлу
        if not os.path.exists(csv_path):
            print("Файл CSV не знайдено!")
            return

        # Читання CSV файлу
        data = pd.read_csv(csv_path)
        if data.empty:
            print("CSV файл порожній!")
            return

        # Додавання колонки "Вік"
        data['Вік'] = data['Дата народження'].apply(calculate_age)

        # Розподіл за віковими категоріями
        younger_18 = data[data['Вік'] < 18]
        age_18_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
        age_45_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
        older_70 = data[data['Вік'] > 70]

        # Створення XLSX файлу
        with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
            # Всі дані
            data.to_excel(writer, sheet_name="all", index=False)
            # Категорії
            younger_18.to_excel(writer, sheet_name="younger_18", index=False)
            age_18_45.to_excel(writer, sheet_name="18-45", index=False)
            age_45_70.to_excel(writer, sheet_name="45-70", index=False)
            older_70.to_excel(writer, sheet_name="older_70", index=False)

        print("Ok, файл XLSX успішно створено!")
    except Exception as e:
        print("Помилка при створенні XLSX файлу:", str(e))

# Використання
csv_file_path = "employees.csv"  # Замініть на ваш шлях до CSV файлу
xlsx_file_path = "employees.xlsx"  # Замініть на бажаний шлях до XLSX файлу
process_csv_to_xlsx(csv_file_path, xlsx_file_path)
