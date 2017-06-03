from functools import reduce
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


def factorial2(n):
    return reduce(lambda a, b : a * b, range(1, n+1))


if __name__ == '__main__':
    for i in range(1, 7):
        print(factorial(i))
        print(factorial2(i))

