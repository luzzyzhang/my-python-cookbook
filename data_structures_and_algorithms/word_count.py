# -*- coding: utf-8 -*-
import sys
from collections import Counter


def word_count(filename):
    wc = {}
    # with open(filename, 'r') as f:
    #     words = f.read().lower().split()
    # for word in words:
    #     if word not in wc:
    #         wc[word] = 1
    #     else:
    #         wc[word] += 1
    # or
    # with open(filename, 'r') as f:
    #     for line in f:
    #         words = line.lower().split()
    #         for word in words:
    #             if word not in words:
    #                 wc[word] = 1
    #             else:
    #                 wc[word] += 1
    # or
    with open(filename, 'r') as f:
        words = f.read().lower().split()
    wc = Counter(words)
    return wc


def print_words(filename):
    wc = word_count(filename)
    # for word, count in sorted(zip(wc.keys(), wc.values())):
    #     print word, count
    # or
    # for word, count in sorted(wc.items()):
    #     print word, count
    # or
    for word, count in sorted(wc.items()):
        print word, count


def print_top(filename, n=20):
    wc = word_count(filename)
    # for count, word in sorted(zip(wc.values(), wc.keys()), reverse=True)[:n]:
    #     print word, count
    # or
    # for word, count in wc.most_common(n):
    #     print word, count
    # or
    for word, count in sorted(wc.items(), key=lambda x: x[1], reverse=True):
        print word, count


def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'Unknow option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
