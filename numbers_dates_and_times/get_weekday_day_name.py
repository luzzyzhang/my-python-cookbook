# -*- coding: utf-8 -*-


import calendar
import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'zh_CN')


now = datetime.now()
print(now.day)
print(list(calendar.day_name))
weekday = calendar.day_name[now.weekday()]
print(weekday)
