# -*- coding: utf-8 -*-

from socket import *


s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 14000))
print(s.recvfrom(128))
print(50*'*')
s.sendto(b'Hello', ('localhost', 15000))
print(s.recvfrom(128))
