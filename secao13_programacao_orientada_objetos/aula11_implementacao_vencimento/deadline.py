#! python
from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.tasks = []
        self.name = name

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description, deadline=None):
        self.tasks.append(Task(description, deadline))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())} pending task(s))'


class Task:
    def __init__(self, description, deadline=None):
        self.description = description
        self.done = False
        self.date = datetime.now()
        self.deadline = deadline

    def completed(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Done)')
        elif self.deadline:
            if datetime.now() > self.deadline:
                status.append('(Expired)')
            else:
                in_day = (self.deadline - datetime.now()).days
                status.append(f'(Will expire in {in_day} days)')
        return f'{self.description}' + ' ' + ''.join(status)


def main():
    house = Project('My tasks 1')
    house.add('To study programming', datetime.now())
    house.add('To read book', datetime.now() + timedelta(days=4, minutes=20))
    house.add('To watch anime')
    house.add('To play game')

    house.search('To watch anime').completed()
    for task in house:
        print(f'- {task}')
    print(house)

    market = Project('My tasks 2')
    market.add('To buy notebook', datetime.now() + timedelta(days=10))
    market.add('To buy mouse')
    market.add('to buy pen')

    to_buy_mouse = market.search('To buy mouse')
    to_buy_mouse.completed()
    for task in market:
        print(f'- {task}')
    print(market)


if __name__ == "__main__":
    main()
