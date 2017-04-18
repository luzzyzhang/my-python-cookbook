# -*- coding: utf-8 -*-


import redis


# r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.Redis(host='localhost', port=6379, db=0)
# r.set('foo', '1')

if not r.get('mytest'):
    r.set('mytest', 1)
    print(r.get('mytest'))
elif int(r.get('mytest')) == 3:
    print('Stop')
    print(r.get('mytest'))
else:
    r.incr('mytest')
    print(r.get('mytest'))
