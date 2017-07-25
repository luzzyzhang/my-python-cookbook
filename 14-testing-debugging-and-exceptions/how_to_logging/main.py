# -*- coding: utf-8 -*-


"""Using logging in multiple modules
`https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook`

1. Multiple calls to logging.getLogger('someLogger')
   return a reference to the same logger object.
2. This is true `not only` within the same module,
   `but also`
   across modules as long as it is in the same Python interpreter process.
"""

import logging

import auxiliary


# create logger with 'my_app'
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug message
fh = logging.FileHandler('debug.log')
feh = logging.FileHandler('error.log')
fh.setLevel(logging.DEBUG)
feh.setLevel(logging.ERROR)

# create console handler with a higher log level
ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
fmt = '%(asctime)s -> %(name)s -> %(levelname)s -> %(message)s'
formatter = logging.Formatter(fmt)
fh.setFormatter(formatter)
feh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(feh)
logger.addHandler(ch)

logger.info('`Creating` an instance of auxiliary.Auxiliary')
a = auxiliary.Auxiliary()
logger.info('`Created` an instance of auxiliary.Auxiliary')
logger.info('`Calling` auxiliary.Auxiliary.do_something')
a.do_something()
logger.info('`Finished` auxiliary.Auxiliary.do_something')
logger.info('`Calling` auxiliary.Auxiliary.something_function()')
auxiliary.some_function()
logger.info('`Done` with auxiliary.some_function()')
logger.error('This is error log for test')

# Test logger
test_logger = logging.getLogger('test')
test_logger.setLevel(logging.DEBUG)

fth = logging.FileHandler('test.log')
fth.setLevel(logging.DEBUG)

fth.setFormatter(logging.Formatter(fmt))

test_logger.addHandler(fth)

test_logger.info('I acccess into your fields')
test_logger.debug('You acccess into your fields')
test_logger.error('She acccess into your fields')







