class Date:
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


date_1 = Date()
date_1.day = 9
date_1.month = 6
date_1.year = 2020
print(date_1)

date_2 = Date()
date_2.day = 10
date_2.month = 6
date_2.year = 2020
print(date_2)
