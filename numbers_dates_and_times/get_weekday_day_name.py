# -*- coding: utf-8 -*-

import calendar
from datetime import datetime


now = datetime.now()
print(list(calendar.day_name))
weekday = calendar.day_name[now.weekday()]
print(weekday)
