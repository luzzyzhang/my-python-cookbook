#!/usr/bin/env/ python3
import argparse
from functools import wraps


def arg_parser(func):
    @wraps(func)
    def parse_it(*args, **kwargs):
        parser = argparse.ArgumentParser(description="My requests for API test")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-sg", "--serverget", action="store_true")
        group.add_argument("-sp", "--serverpost", action="store_true")
        parser.add_argument("api", help="the api name")

        input_args = parser.parse_args()
        r = func(input_args, *args, **kwargs)
        return r
    return parse_it


if __name__ == '__main__':
    @arg_parser
    def foo(*args, **kwargs):
        custom = args[0]
        if custom.serverget:
            print('a')
        elif custom.serverpost:
            print('b')
        else:
            print('c')
        api_params_map = {'test': 'Just for fun'}
        if custom.api:
            print(api_params_map.get(custom.api, 'Nont found'))
        return 'ok'
    r = foo()
