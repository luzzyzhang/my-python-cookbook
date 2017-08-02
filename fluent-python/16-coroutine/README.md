- The *behavior* and *states* of a generator operating as a coroutine.
- Priming a coroutine automatically with a decorator.
- How the caller can control a coroutine through the `.close()` and `.throw()` methods of the generator object
- How coroutines can return values upon termination.
- Usage and semantics of the new `yield from` syntax.
- A use case: coroutines for managing concurrent activities in simulation.
---
## Basic behavior of `generator` used as `coroutine`

```python
>>> def simple_coroutine():
...     print('-> coroutine started')
...     x = yield
...     print('-> coroutine received:', x)
>>> my_coro = simple_coroutine()
>>> my_coro
<generator object simple_coroutine at 0x10e8d0bf8>
>>> next(my_coro)
-> coroutine started
>>> my_coro.send(123)
-> coroutine received: 42
Traceback (most recent call last):
    ...
StopIteration
``` 

> A `coroutine` can be in one of four states. `inspect.getgeneratorstate(...)` -> one of the strings:

> `GEN_CREATED`: Waiting to start execution.

> `GEN_RUNNING`: Currently being executed by the interpreter.(You’ll only see this state in a multi-threaded application — or if the generator object calls getgenerator state on itself, which is not useful.)

> `GEN_SUSPENDED`: Currently suspended at a yield expression.

> `GEN_CLOSED`: Execution has completed.


```python
>>> def simple_coro2(a):
...     print('-> Started: a =', a)
...     b = yield a
...     print('-> Received: b =', b)
...     c = yield a + b
...     print('-> Received: c =', c)
...
>>> my_coro2 = simple_coro2(14)
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(my_coro2)
'GEN_CREATED'
>>> next(my_coro2)
-> Started: a = 14
14
>>> getgeneratorstate(my_coro2)
'GEN_SUSPENDED'
>>> my_coro2.send(28)
-> Recevied: b = 28
42
>>> my_coro2.send(99)
-> Received: c = 99
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
StopIteration
>>> getgeneratorstate(my_coro2)
'GEN_CLOSED'
```

---

## Further reading
[Coroutine Wikipedia](https://zh.wikipedia.org/wiki/%E5%8D%8F%E7%A8%8B)

[A Curious Course on Coroutines and Concurrency by David Beazley](http://www.dabeaz.com/coroutines/)

[Tasks and coroutines](https://docs.python.org/3/library/asyncio-task.html)
