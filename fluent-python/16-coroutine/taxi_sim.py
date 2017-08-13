# -*- coding: utf-8 -*-
"""
Taxi simulator with delay on output
===================================
This is a variation of ``taxi_sim.py`` which adds a ``-d`` comand-line
option. When given, that option adds a delay in the main loop, pausing
the simulation for .5s for each "minute" of simulation time.
Driving a taxi from the console::
    >>> from taxi_sim import taxi_process
    >>> taxi = taxi_process(ident=13, trips=2, start_time=0)
    >>> next(taxi)
    Event(time=0, proc=13, action='leave garage')
    >>> taxi.send(_.time + 7)
    Event(time=7, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 23)
    Event(time=30, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 5)
    Event(time=35, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 48)
    Event(time=83, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=84, proc=13, action='going home')
    >>> taxi.send(_.time + 10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
Sample run with two cars, random seed 10. This is a valid doctest::
    >>> main(num_taxis=2, seed=10)
    taxi: 0  Event(time=0, proc=0, action='leave garage')
    taxi: 0  Event(time=5, proc=0, action='pick up passenger')
    taxi: 1     Event(time=5, proc=1, action='leave garage')
    taxi: 1     Event(time=10, proc=1, action='pick up passenger')
    taxi: 1     Event(time=15, proc=1, action='drop off passenger')
    taxi: 0  Event(time=17, proc=0, action='drop off passenger')
    taxi: 1     Event(time=24, proc=1, action='pick up passenger')
    taxi: 0  Event(time=26, proc=0, action='pick up passenger')
    taxi: 0  Event(time=30, proc=0, action='drop off passenger')
    taxi: 0  Event(time=34, proc=0, action='going home')
    taxi: 1     Event(time=46, proc=1, action='drop off passenger')
    taxi: 1     Event(time=48, proc=1, action='pick up passenger')
    taxi: 1     Event(time=110, proc=1, action='drop off passenger')
    taxi: 1     Event(time=139, proc=1, action='pick up passenger')
    taxi: 1     Event(time=140, proc=1, action='drop off passenger')
    taxi: 1     Event(time=150, proc=1, action='going home')
    *** end of events ***
"""

import time
import queue
import random
import argparse
import collections


DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(ident, trips, start_time=0):
    """Yield to simulator issuing event at each state change"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')


class Simulator:

    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time, delay=False):
        """Schedule and display events unitl time is up"""
        # schedule the first event for each cab
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        # main loop of the simulation
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            # get and display current event
            current_event = self.events.get()
            if delay:
                time.sleep((current_event.time - sim_time) / 2)
            # update the simulation time
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id*'  ', current_event)
            active_proc = self.procs[proc_id]
            # schedule next action for current proc
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))


def compute_duration(previous_action):
    """Compute action duration using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state is prowling
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state is trip
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknow previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1


def main(end_time=DEFAULT_END_TIME,
         num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None, delay=False):
    """Initialize random generator, build procs and run simulation"""
    if seed is not None:
        random.seed(seed)  # ger reproducible results
    taxis = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time, delay)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Taxi fleet simulator.')

    parser.add_argument(
        '-e', '--end-time', type=int, default=DEFAULT_END_TIME,
        help='simulation end time; default = %s' % DEFAULT_END_TIME
    )
    parser.add_argument(
        '-t', '--taxis', type=int, default=DEFAULT_NUMBER_OF_TAXIS,
        help='number of taxis running; default = %s' % DEFAULT_NUMBER_OF_TAXIS
    )
    parser.add_argument(
        '-s', '--seed', type=int, default=None,
        help='random generator seed (for testing)'
    )
    parser.add_argument(
        '-d', '--delay', action='store_true',
        help='introduce delay proportional to simulation time'
    )
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed, args.delay)
