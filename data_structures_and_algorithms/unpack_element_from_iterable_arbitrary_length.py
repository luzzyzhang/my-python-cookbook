# Need unpack N elements but the iterable may be longer than N
# Use "star expression" only work Python3


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

records = ('Dave', 'dave@gmail.com', '122-3328-8697', '133-3328-8697')
name, email, *phone_numbers = records
print(name)
print(email)
print(phone_numbers)
sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record
print(trailing_qtrs)
print(50*'*')
print(current_qtr)
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# print(avg_comparison(trailing_avg, current_qtr))
records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    if tag == 'bar':
        do_bar(args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty/:/usr/bin/false'
uname, *files, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)
