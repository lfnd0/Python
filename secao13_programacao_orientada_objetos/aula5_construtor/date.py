class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


date_1 = Date(12, 6, 2020)
print(date_1)

date_2 = Date(13, 6, 2020)
print(date_2)

date_3 = Date(year=2020, month=6)
print(date_3)

date_4 = Date()
print(date_4)
