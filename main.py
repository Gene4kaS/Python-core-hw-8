from datetime import datetime, timedelta


def get_birthdays_per_week(users: list) -> None:
    today = datetime.now()
    day_interval = days_interval(today)
    new_time_line = today + day_interval

    week = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    
    for user in users:
        new_date_for_user = datetime(
            year=today.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )        
       
        if today <= new_date_for_user <= new_time_line:
            day = new_date_for_user.strftime('%A')

            if day in ['Saturday', 'Sunday']:
                day = 'Monday'
            week.get(day).append(user.get('name')) 

    print_users_list(week)

def days_interval(today: datetime) -> timedelta:
    if today.weekday() == 5:
        day_interval = timedelta(days=6)
    elif today.weekday() == 6:
        day_interval = timedelta(days=5)
    else:
        day_interval = timedelta(days=7)
    #print(day_interval)
    return day_interval
    


def print_users_list(week: dict):
    for key, value in week.items():
        if value:
            print(f"{key}: {', '.join(value)}")

persons_birthdays = [
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
    {"name": "Ivan", "birthday": datetime(2000, 12, 6)
    }
    ]

    
if __name__ == '__main__':
    get_birthdays_per_week(persons_birthdays)