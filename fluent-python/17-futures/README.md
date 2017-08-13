## Examples: Web download in three style
> `flags.py` runs sequentially: it onley requests the next image when the previous one is downloaded and saved to disk.
> `flags_threadpool.py`, `flags_asyncio.py` make concurrent downloads: they request all images practically at the same time, and save the files as they arrive.
> The `flags_threadpool.py` uses the `concurrent.futures` package, while `flags_asyncio.py` uses `asyncio`.

> A common refactoring when writing concurrent code: turning _the body of_ a sequential for loop _into a function_ to be called concurrently.

## About the `future`
> There are two classes named `Future` in the standard library: `concurrent.futures.Future` and `asyncio.Future`. 
> They **serve the same purpose: an instance of either `Future` class represents a deferred computation that may or may not have completed.**

## Good questions
> Strictly speaking, none of the concurrent scripts we tested so far can perform downloads in parallel.

> The `concurrent.futures` examples are limited by the **`GIL`**, and the `flags_asyncio.py` is _single-threaded_.

- How can `flags_threadpool.py` perform 5x faster than `flags.py` if Python threads are limited by a `GIL(Global Interpreter Lock)` _that only lets one thread run at any time_? [Why the GIL is nearly harmless with I/O bound processing.](#blocking-io-and-the-gil)
- How can `flags_asyncio.py` perform 5x faster than `flags.py` when both are single threaded?

## Blocking I/O and the GIL
> The CPython interpreter is **not thread-safe internally**, 
> so it has a **Global Interpreter Lock (GIL)** which allows only one thread at a time to execute Python bytecodes. 
> That’s why a single Python process usually cannot use multiple CPU cores at the same time

>When we write Python code we have no control over the GIL, but a built-in function or an extension written in C can release the GIL while running time consuming tasks. In fact, a Python library coded in C can manage the GIL, launch its own OS threads and take advantage of all available CPU cores. This complicates the code of the library con‐ siderably, and most library authors don’t do it.
