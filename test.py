from datetime import datetime, timedelta
from copy import deepcopy


WEEK = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}


def get_birthdays_per_week(users: list) -> None:
    today = datetime.now()  # сьогоднішня дата

    start_current_week = (today - timedelta(2 + today.weekday()))  # дата початку цього тижня (не з понеділка, а з суботи минулого)
    end_current_week = (today + timedelta(4 - today.weekday()))  # дата кінця поточного тижня (п'ятниця)
    end_next_week = (today + timedelta(4 - today.weekday() + 7))  # дата кінця наступного тижня (п'ятниця)

    this_week = deepcopy(WEEK)
    next_week = deepcopy(WEEK)

    for user in users:
        birthday: datetime = user["birthday"].replace(year=today.year)

        if datetime(today.year, 1, 7) >= today:
            if birthday.month == 12 and birthday > datetime(today.year, 1, 1):
                birthday = birthday.replace(year=today.year-1)

        elif datetime(today.year, 12, 24) <= today:
            if birthday.month == 1 and birthday > datetime(today.year, 1, 1):
                birthday = birthday.replace(year=today.year+1)

        if (birthday >= start_current_week) and (birthday <= end_next_week):
            name_weekday = "Monday" if birthday.weekday() in (5, 6) else birthday.strftime("%A")

            if birthday < end_current_week:
                this_week[name_weekday].append(user['name'])

            else:
                next_week[name_weekday].append(user['name'])

    report_birthday(
        this_week,
        "{} - {}".format(start_current_week.strftime("%d.%m.%Y"), end_current_week.strftime("%d.%m.%Y"))
    )

    report_birthday(
        next_week,
        "{} - {}".format(end_current_week.strftime("%d.%m.%Y"), end_next_week.strftime("%d.%m.%Y"))
    )


def report_birthday(week: dict, dates: str) -> None:
    week = ["{:<11}: {}".format(day, ', '.join(names)) for day, names in week.items() if names]

    if week:
        print('\n' + dates)

        for day in week:
            print(day)


USERS = [
    {'name': 'Jim', 'birthday': datetime(1975, 12, 6)},
    {'name': 'Miranda', 'birthday': datetime(2010, 12, 10)},
    {'name': 'Ricardo', 'birthday': datetime(2001, 12, 3)},
    {'name': 'Viktoria', 'birthday': datetime(2005, 12, 12)},
    {'name': 'Miranda', 'birthday': datetime(2003, 12, 4)},
    {'name': 'Anna', 'birthday': datetime(2002, 12, 5)},
    {'name': 'Perry', 'birthday': datetime(1985, 12, 7)},
    {'name': 'Mike', 'birthday': datetime(1999, 12, 15)},
    {'name': 'Robin', 'birthday': datetime(1980, 11, 30)},
    {'name': 'Vika', 'birthday': datetime(2000, 12, 8)},
    {"name": "Taras", "birthday": datetime(1999, 12, 7)},
    {"name": "Olha", "birthday": datetime(1999, 12, 10)},
    {"name": "Iryna", "birthday": datetime(1994, 12, 3)},
    {"name": "Maksym", "birthday": datetime(1997, 12, 8)},
    {"name": "Dmytro", "birthday": datetime(1993, 12, 16)},
    {"name": "Ivan", "birthday": datetime(2000, 12, 6)}
]


if __name__ == '__main__':
    get_birthdays_per_week(USERS)