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

> A `coroutine` can be in one of four states. `inspect.generatorstate(...)` -> one of the strings:

> `GEN_CREATE`: Waiting to start execution.

> `GEN_RUNNING`: Currently being executed by the interpreter.

> `GEN_SUSPENDED`: Currently suspended at a yield expression.

> `GEN_CLOSED`: Execution has completed.

---

## Further reading
[Coroutine Wikipedia](https://zh.wikipedia.org/wiki/%E5%8D%8F%E7%A8%8B)

[A Curious Course on Coroutines and Concurrency by David Beazley](http://www.dabeaz.com/coroutines/)

[Tasks and coroutines](https://docs.python.org/3/library/asyncio-task.html)
