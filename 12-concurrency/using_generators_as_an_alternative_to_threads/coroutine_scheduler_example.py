# -*- coding: utf-8 -*-

"""
    Simple example of a coroutine/generator scheduler
    ~~~~~~
    Generator functions are the tasks,
    and the yield statement is how tasks signal that they want to suspend.
    The scheduler simply cycles over the tasks until none are left executing.
"""

from collections import deque


def countdown(n):
    while n > 0:
        print("T-minus", n)
        yield
        n -= 1
    print('Blastoff!')


def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1


class TaskScheduler:

    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        # Admit a newly started task to the scheduler
        self._task_queue.append(task)

    def run(self):
        # Run unitl there are no more task
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass


if __name__ == '__main__':
    sched = TaskScheduler()
    sched.new_task(countdown(10))
    sched.new_task(countdown(5))
    sched.new_task(countup(15))
    print(sched._task_queue)
    sched.run()
