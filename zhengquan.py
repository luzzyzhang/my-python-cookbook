# -*- coding: utf-8 -*-

import json
from pprint import pprint
import requests

my_ak = 'kdPVvSv7n0BZl70MQgDPiQ9U6WQfeYHp'
playload = {'q': '证券营业部', 'region': '北京市', 'output': 'json',
            'ak': my_ak, 'page_num': 2, 'page_size': 20}
r = requests.get('http://api.map.baidu.com/place/v2/search', params=playload)
data = r.json()
pprint(data)
print([(d['name'], d['address'], d.get('telephone')) for d in data['results']])
# data = json.load(open('data_out.json'))
# print(len(data['content']))
# print(data['content'][8]['name'])
# print(data['content'][8]['addr'])
# pprint(data['content'][8]['ext']['detail_info']['phone'])
# print(json.dumps(data, ensure_ascii=False), file=open('r.txt', 'w'))
