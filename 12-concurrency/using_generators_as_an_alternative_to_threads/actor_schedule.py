# -*- coding: utf-8 -*-

import time
from collections import deque


class ActorScheduler:

    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        # Admit a newly started actor to the scheduler and give it name
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send_msg(self, name, msg):
        # Send a message to a named actor
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        # Run as long as there are pending messages.
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


if __name__ == '__main__':

    def printer():
        while True:
            msg = yield
            print('Got:', msg)

    def counter(sched):
        while True:
            # Receive the current counter
            n = yield
            if n == 0:
                break
            # Send to the printer task
            sched.send_msg('printer', n)
            # Send the next counter to the counter task (recursive)
            sched.send_msg('counter', n-1)

    sched = ActorScheduler()
    # Create the inital actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    # Send an initial message to the counter to initiate
    sched.send_msg('counter', 10000)
    print(sched._msg_queue)
    sched.run()
