
## `Context Manager`
**Copy from `Kenneth Reitz's Hitchhiker Guide to Python Context Manager` and `Luciano Ramalho's book`**
    

> A context manager is a Python object that provides extra contextual information to an action.

> An object implementing both the `__enter__` and `__exit__` special methods, for use in a `with` block.

> This extra information takes the form of running a callable upon initiating the context using the with statement, as well as running a callable upon completing all the code inside the `with` block

```python
class CustomOpen(object):
    def __init__(self, filename):
	self.file = open(filename)

    def __enter__(self):
	return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
	self.file.close()

    with CustomOpen('file') as f:
	    contents = f.read()
```
    
`Generator approach using Python’s own contextlib`

> In a generator decorated with @contextmanager, yield is used to split the body of the function in two parts: everything before the yield will be executed at the beginning of the while block when the interpreter calls `__enter__`; the code after yield will run when `__exit__` is called at the end of the block.


```python
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
	yield f
    finally:
	f.close()

with custom_open('file') as f:
    contents = f.read() 
```


## Further reading
[Hitchhiker Guide to Python Context Manager by Kenneth Reitz](http://python-guide-pt-br.readthedocs.io/en/latest/writing/structure/#context-managers)
