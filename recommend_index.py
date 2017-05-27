def test(lst, n):
    t = max(lst) - min(lst)
    h = round(t / 5)
    lst = sorted(set(lst))
    print(lst)
    for i in range(5):
        if n in lst[i*h: (i+1)*h]:
            print('Get {} start'.format(i+1))


if __name__ == '__main__':
    from random import randint
    # lst = [randint(3, 20) for _ in range(30)]
    # print(lst)
    lst = [13, 16, 17, 12, 10, 9, 14, 12, 11, 9, 16, 9, 13, 7, 13, 17, 11, 4, 3, 12, 4, 11, 8, 6, 11, 9, 19, 15, 4, 16]
    test(lst, 9)
    test(lst, 3)
