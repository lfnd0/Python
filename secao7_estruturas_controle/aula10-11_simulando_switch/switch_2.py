def get_type_day(day):
    type_days = {
        1: 'weekend',
        2: 'week',
        3: 'week',
        4: 'week',
        5: 'week',
        6: 'week',
        7: 'weekend'
    }
    return type_days.get(day, 'invalid')


if __name__ == "__main__":
    for day in range(8):
        print(f'{day}: {get_type_day(day)}')
