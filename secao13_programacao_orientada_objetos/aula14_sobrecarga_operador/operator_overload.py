#! python
from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.tasks = []
        self.name = name

    def __iter__(self):
        return self.tasks.__iter__()

    # Sobrecarga do operador '+='
    def __iadd__(self, task):
        task.owner = self
        self._add_task(task)
        return self

    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, description, **kwargs):
        self.tasks.append(Task(description, kwargs.get('deadline', None)))

    def add(self, task, deadline=None, **kwargs):
        chosen_function = self._add_task if isinstance(
            task, Task) else self._add_new_task
        kwargs['deadline'] = deadline
        chosen_function(task, **kwargs)

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
                day = (self.deadline - datetime.now()).days
                status.append(f'(Will expire in {day} days)')
        return f'{self.description}' + ' ' + ''.join(status)


class RecurringTask(Task):
    def __init__(self, description, deadline, in_day=7):
        super().__init__(description, deadline)
        self.in_day = in_day
        self.owner = None

    def completed(self):
        super().completed()
        new_deadline = datetime.now() + timedelta(days=self.in_day)
        new_task = RecurringTask(self.description, new_deadline, self.in_day)
        if self.owner:
            self.owner += new_task
        return new_task


def main():
    house = Project('My tasks 1')
    house.add('To study programming', datetime.now())
    house.add('To read book')
    house.add('To watch anime')
    house.add('To play game')
    house += RecurringTask('To write TCC', datetime.now(), 7)
    house.search('To write TCC').completed()

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
