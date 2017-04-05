# -*- coding: utf-8 -*-

import json
from pprint import pprint
import requests

my_ak = 'kdPVvSv7n0BZl70MQgDPiQ9U6WQfeYHp'
playload = {'q': '证券营业部', 'region': '北京市', 'output': 'json',
            'ak': my_ak, 'page_num': 0, 'page_size': 20}
r = requests.get('http://api.map.baidu.com/place/v2/search', params=playload)
data = r.json()
page_nums = data['total'] // 20
result = []
for i in range(page_nums):
    playload['page_num'] = i
    r = requests.get('http://api.map.baidu.com/place/v2/search', params=playload)
    r = r.json()['results']
    result.append((d['name'], d.get('telephone'), d['address']) for d in r if d.get('telephone'))
print(list(result))
with open('r.txt', 'w') as f:
    header = "{}, {:>10s}, {:>10s} \n".format('营业部名', '电话', '地址')
    f.write(header)
    for l in result:
        for i in l:
            info = "{}, {:>10s}, {:>10s} \n".format(*i)
            f.write(info)
# print([(d['name'], d['address'], d.get('telephone')) for d in data['results']])
# data = json.load(open('data_out.json'))
# print(len(data['content']))
# print(data['content'][8]['name'])
# print(data['content'][8]['addr'])
# pprint(data['content'][8]['ext']['detail_info']['phone'])
# print(json.dumps(data, ensure_ascii=False), file=open('r.txt', 'w'))
