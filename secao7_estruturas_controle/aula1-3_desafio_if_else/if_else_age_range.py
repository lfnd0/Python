def age_range(age):
    if 0 <= age < 18:
        return 'Minor'
    elif age in range(18, 64):
        return 'Adult'
    elif age in range(65, 100):
        return 'Aged'
    elif age > 100:
        return 'Centenarian'
    else:
        return 'Invalid age'


if __name__ == "__main__":
    for age in (17, 35, 87, 113, -1):
        print(f'{age}: {age_range(age)}')
