#! python
from datetime import datetime


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
    house = []
    house.append(Task('To watch anime'))
    house.append(Task('To study programming'))
    house.append(Task('To play game'))
    house.append(Task('To read book'))

    [task.completed() for task in house if task.description == 'To watch anime']
    for task in house:
        print(f'- {task}')


if __name__ == "__main__":
    main()
