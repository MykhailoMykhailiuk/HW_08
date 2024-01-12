from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):

    # Реалізуйте тут домашнє завдання
    if not users:
        return {}
    
    result_dict = {}
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    result_dict = dict.fromkeys(day_of_week, [])

    current_day = date.today()

    interval = timedelta(days=6)

    for user in users:

        bd_year = user['birthday'].replace(year=current_day.year)

        # Якщо день народження пройшов - переносимо на наступний рік
        if current_day > bd_year:
            bd_year = bd_year.replace(year=current_day.year + 1)

        # Якщо день народження Субота або Неділя - переносимо на Понеділок
        if bd_year.weekday() == 5:
            bd_year += timedelta(days=2)
        elif bd_year.weekday() == 6:
            bd_year += timedelta(days=1)
                   
        week_day = bd_year.strftime('%A')
        
        # Перевіпяємо чи день народження в діапазоні 7 днів
        if current_day <= bd_year <= (current_day + interval):

            result_dict[week_day] = [user['name']] + result_dict.get(week_day, [])  # noqa: E501
    
    # Видаляємо порожні дні зі словника
    result_dict = {key: value for key, value in result_dict.items() if value != []}  # noqa: E501

    if 'Monday' in result_dict:
        result_dict['Monday'].reverse()

    return result_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 11).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 1, 12).date()},
        {"name": "Dave Jones", "birthday": datetime(1976, 1, 13).date()},
        {"name": "Carolina Smith", "birthday": datetime(1985, 1, 14).date()},
        {"name": "Ashly Wood", "birthday": datetime(1969, 1, 2).date()},
        {"name": "Grant Tompson", "birthday": datetime(1994, 1, 24).date()},
        {"name": "Tomas Yang", "birthday": datetime(1982, 1, 30).date()},
        {"name": "Loo Kang", "birthday": datetime(1985, 1, 10).date()},
        {"name": "Ban Wolsh", "birthday": datetime(1976, 1, 17).date()},
        {"name": "Brandon Roswel", "birthday": datetime(1991, 1, 5).date()},
        {"name": "Gareth Filch", "birthday": datetime(1986, 1, 5).date()},
        {"name": "Amanda Jonson", "birthday": datetime(1965, 1, 9).date()},
        {"name": "Grag McCall", "birthday": datetime(1979, 11, 19).date()},
        {"name": "Lilly James", "birthday": datetime(1981, 1, 7).date()},
        {"name": "Bob Westbrok", "birthday": datetime(1987, 5, 23).date()},
        {"name": "James Nicols", "birthday": datetime(1999, 9, 4).date()},
        {"name": "Lois Lane", "birthday": datetime(1969, 4, 9).date()},
        {"name": "Barry Allen", "birthday": datetime(1993, 1, 7).date()},
        {"name": "Bruce Wane", "birthday": datetime(1994, 6, 12).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
