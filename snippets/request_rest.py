#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
playload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=playload)
print(r.text)
