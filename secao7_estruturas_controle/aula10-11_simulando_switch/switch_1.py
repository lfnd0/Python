def get_day_week(day):
    days_week = {
        1: 'sunday',
        2: 'monday',
        3: 'tuesday',
        4: 'wednesday',
        5: 'thursday',
        6: 'friday',
        7: 'saturday'
    }
    return days_week.get(day, 'invalid')


if __name__ == "__main__":
    for day in range(0, 9):
        print(f'{day}: {get_day_week(day)}')
