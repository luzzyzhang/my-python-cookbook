# -*- coding: utf-8 -*-


def binary_search(lst, t):
    left, right = 0, len(lst) - 1
    while left <= right:
        # mid = (left+right) / 2
        mid = left + (right-left) // 2
        if lst[mid] < t:
            left = mid + 1
        elif lst[mid] > t:
            right = mid - 1
        else:
            return mid
    return False


# Search lst(sorted and have duplicate elements) return first t's index
# Example: lst = [0, 2, 2, 3], t = 2, return index is 1
def binary_search_first_index(lst, t):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = left + (right-left)//2
        if lst[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    if left < len(lst) and lst[left] == t:
        return left
    else:
        return False


# Example: lst = [0, 2, 2, 3], t = 2, return index is 2
def binary_search_last_index(lst, t):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] > t:
            right = mid - 1
        else:
            left = mid + 1

    if right < len(lst) and lst[right] == t:
        return right
    else:
        return False


if __name__ == '__main__':
    lst = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8]
    print lst
    print 60*'*'
    print binary_search(lst, 2)
    print 50*'-'
    print binary_search(lst, 3)
    print 50*'-'
    print binary_search(lst, 9)
    print 50*'~'
    print binary_search_first_index(lst, 2)
    print binary_search_first_index(lst, 3)
    print binary_search_first_index(lst, 9)
    print 50*'.'
    print binary_search_last_index(lst, 2)
    print binary_search_last_index(lst, 3)
    print binary_search_last_index(lst, 9)
