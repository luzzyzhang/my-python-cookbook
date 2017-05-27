# -*- coding: utf-8 -*-


import redis


# r = redis.StrictRedis(host='localhost', port=6379, db=0)
r = redis.Redis(host='localhost', port=6379, db=0)
# r.set('foo', '1')

if not r.get('lr'):
    r.set('lr', 1)
    print(r.get('lr'))
elif int(r.get('lr')) == 3:
    print('Stop')
    print('Now you have get {} times play'.format(int(r.get('lr'))))
else:
    r.incr('lr')
    print(r.get('lr'))
