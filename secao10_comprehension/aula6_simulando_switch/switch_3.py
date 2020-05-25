def get_type_day(day):
    days = {
        (1, 7): 'weekend',
        tuple(range(2, 7)): 'week'
    }

    # Generator 'chosen_day' retorna o 'type_day'
    chosen_day = (type_day for numbers,
                  type_day in days.items() if day in numbers)

    return next(chosen_day, 'invalid')


if __name__ == "__main__":
    for day in range(0, 9):
        print(f'{day}: {get_type_day(day)}')
