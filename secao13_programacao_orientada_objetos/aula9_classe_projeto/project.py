#! python
from datetime import datetime


class Project:
    def __init__(self, name):
        self.tasks = []
        self.name = name

    def add(self, description):
        self.tasks.append(Task(description))

    def pending(self):
        return [task for task in self.tasks if not task.done]

    def search(self, description):
        return [task for task in self.tasks if task.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())} pending task(s))'


class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.date = datetime.now()

    def completed(self):
        self.done = True

    def __str__(self):
        return self.description + ' ' + ('(Done)' if self.done else '')


def main():
    house = Project('My tasks 1')
    house.add('To watch anime')
    house.add('To study programming')
    house.add('To play game')
    house.add('To read book')

    house.search('To watch anime').completed()
    for task in house.tasks:
        print(f'- {task}')
    print(house)

    market = Project('My tasks 2')
    market.add('To buy mouse')
    market.add('To buy notebook')
    market.add('to buy pen')

    to_buy_mouse = market.search('To buy mouse')
    to_buy_mouse.completed()
    for task in market.tasks:
        print(f'- {task}')
    print(house)


if __name__ == "__main__":
    main()
