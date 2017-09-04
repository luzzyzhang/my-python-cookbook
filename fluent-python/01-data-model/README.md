

> One of the best qualities of Python is its consistency.

>The Python interpreter invokes special methods to perform basic object oper‐ ations, often triggered by special syntax. The special method names are always spelled with leading and trailing double underscores, i.e. `__getitem__`.

> obj[key] is supported by the `__getitem__` special method. To evaluate my_collec tion[key], the interpreter calls `my_collection`.`__getitem__`(key).

> Special method also called Magic method or dunder method, `__getitem__` pronouncing as `dunder-getitem`

**How special methods are used**
> The first thing to know about special methods is that they are meant to be called by the Python interpreter, and not by you. You don’t write my_object.`__len__`(). You write len(my_object) and, if my_object is an instance of a user defined class, then Python calls the `__len__` instance method you implemented.

> But for built-in types like list, str, bytearray etc., the interpreter takes a shortcut: the CPython implementation of len() actually returns the value of the ob_size field in the PyVarObject C struct that represents any variable-sized built-in object in memory. This is much faster than calling a method.

> More often than not, the special method call is implicit. For example, the statement for i in x: actually causes the invocation of iter(x) which in turn may call x.`__iter__`() if that is available.
Normally, your code should not have many direct calls to special methods. Unless you are doing a lot of metaprogramming, you should be implementing special methods more often than invoking them explicitly. The only special method that is frequently called by user code directly is `__init__`, to invoke the initializer of the superclass in your own `__init__` implementation.
If you need to invoke a special method, it is usually better to call the related built-in function, such as len, iter, str etc. These built-ins call the corresponding special method, but often provide other services and — for built-in types — are faster than method calls.

> Avoidcreatingarbitrary,customattributeswiththe__foo__syntaxbecausesuchnames may acquire special meanings in the future, even if they are unused today.

> **By implementing special methods, __your objects__ can behave like the built-in types, en‐sabling the expressive coding style the community considers Pythonic**.
A basic requirement for a Python object is to provide usable string representations of itself, one used for debugging and logging, another for presentation to end users. That is why the special methods `__repr__` and `__str__` exist in the Data Model.
