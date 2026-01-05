import datetime

# Функция проверки високосного года
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Функция определения дня недели
def get_weekday(day, month, year):
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    weekday_num = datetime.date(year, month, day).weekday()
    return weekdays[weekday_num]

# Функция расчёта возраста
def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year

# Преобразование цифры в «табло» из звёздочек
def digit_to_stars(digit):
    patterns = {
        '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        '1': ['  *  ', '  *  ', '  *  ', '  *  ', '  *  '],
        '2': [' *** ', '    *', ' *** ', '*    ', ' *** '],
        '3': [' *** ', '    *', ' *** ', '    *', ' *** '],
        '4': ['*   *', '*   *', ' *** ', '    *', '    *'],
        '5': [' *** ', '*    ', ' *** ', '    *', ' *** '],
        '6': [' *** ', '*    ', ' *** ', '*   *', ' *** '],
        '7': [' *** ', '    *', '    *', '    *', '    *'],
        '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
        '9': [' *** ', '*   *', ' *** ', '    *', ' *** ']
    }
    return patterns[digit]

# Вывод числа (даты) в виде «табло»
def number_to_stars(number):
    lines = [[] for _ in range(5)]  # 5 строк для каждой цифры
    for digit in str(number):
        digit_pattern = digit_to_stars(digit)
        for i, line in enumerate(digit_pattern):
            lines[i].append(line)
    return [' '.join(line) for line in lines]

# Основная программа
print("Введите дату рождения:")
try:
    day = int(input("День (1-31): "))
    month = int(input("Месяц (1-12): "))
    year = int(input("Год: "))

    # Проверка корректности даты
    datetime.date(year, month, day)

    # Вычисляем и выводим результаты
    weekday = get_weekday(day, month, year)
    leap_year = is_leap_year(year)
    age = calculate_age(year)

    print(f"\nРезультаты:")
    print(f"День недели: {weekday}")
    print(f"Високосный год: {'Да' if leap_year else 'Нет'}")
    print(f"Ваш возраст: {age} лет")

    # Формируем и выводим дату в формате «дд мм гггг» в виде звёздочек
    birth_date = f"{day:02d}{month:02d}{year}"
    print("\nДата рождения (в формате дд мм гггг, как на табло):")
    for line in number_to_stars(birth_date):
        print(line)

except ValueError as e:
    if "invalid literal" in str(e):
        print("Ошибка: введите только числа!")
    else:
        print("Некорректная дата! Проверьте значения дня, месяца или года.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
