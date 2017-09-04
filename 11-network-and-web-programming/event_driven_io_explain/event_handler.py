# -*- coding: utf-8 -*-

import select


class EventHandler:

    def fileno(self):
        """Return the associated file descriptor"""
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        """Return True if receving is allowed"""
        return False

    def handle_receive(self):
        """Perform the revevie operation"""
        pass

    def wants_to_send(self):
        """Return True if sending is requested"""
        return False

    def handle_send(self):
        """Send outgoing data"""
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()
