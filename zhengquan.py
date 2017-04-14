# -*- coding: utf-8 -*-

# import json
# from pprint import pprint
import requests

my_ak = 'kdPVvSv7n0BZl70MQgDPiQ9U6WQfeYHp'
api = 'http://api.map.baidu.com/place/v2/search'
playload = {'q': '证券营业部', 'region': '北京市', 'output': 'json',
            'ak': my_ak, 'page_num': 0, 'page_size': 20}
r = requests.get(api, params=playload)
data = r.json()
result = []
page_nums = data['total'] // 20


for i in range(page_nums):
    playload['page_num'] = i
    r = requests.get(api, params=playload)
    r = r.json()['results']
    result.append((d['name'], d.get('telephone'), d['address'])
                  for d in r if d.get('telephone'))

with open('r.txt', 'w') as f:
    header = "{}, {:>10s}, {:>10s} \n".format('营业部名', '电话', '地址')
    f.write(header)
    for l in result:
        for i in l:
            info = "{}, {:>10s}, {:>10s} \n".format(*i)
            f.write(info)
