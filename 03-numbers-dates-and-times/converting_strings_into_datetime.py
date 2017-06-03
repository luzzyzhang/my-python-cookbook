# -*- coding: utf-8 -*-


from datetime import datetime


text = '2017-05-03'
y = datetime.strptime(text, '%Y-%m-%d')
now_time = datetime.now()
now_date = datetime.now().date()
diff = now_time - y
print(y)
print(now_time)
print(now_date)
print(diff)

date_to_str = datetime.strftime(now_date, '%A %B %d, %Y')
print(date_to_str)


def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))

print(parse_ymd('1991-11-11'))
