# -*- coding: utf-8 -*-
import json

test_dict = {'a': 1, 'b': 2, 'c': 3}
# python2, python3.5, python3.6
print(json.dumps(test_dict))
print(json.dumps(test_dict, sort_keys=True))
