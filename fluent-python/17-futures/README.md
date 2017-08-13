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
> That’s why a single Python process usually cannot use multiple CPU cores at the same time.

> When we write Python code we have no control over the GIL, but a built-in function or an extension written in C can release the GIL while running time consuming tasks. In fact, a Python library coded in C can manage the GIL, launch its own OS threads and take advantage of all available CPU cores. This complicates the code of the library con‐ siderably, and most library authors don’t do it.

> **However**, _all standard library functions_ that **perform blocking I/O** _release the GIL_ **when waiting for a result from the OS**. This means Python programs that are I/O bound can benefit from using threads at the Python level: while one Python thread is waiting for a response from the network, the blocked I/O function releases the GIL so another thread can run.

> Every blocking I/O function in the Python standard library releases the GIL, allowing other threads to run. The time.sleep() function also releases the GIL. _**Therefore, Python threads are perfectly usable in I/O bound applications, despite the GIL.**_

## Launching processes (_truly parallel tasks_)
> _Launching parallel tasks_. The package does enable **truly parallel computations** _because it supports distributing work among **multiple Python processes** using the `ProcessPoolExecutor` class_ — thus bypassing the GIL and leveraging all available CPU cores, if you need to do **`CPU-bound processing`**.

## `ProcessPoolExecutor` and `ThreadPoolExecutor`
> Both `ProcessPoolExecutor` and `ThreadPoolExecutor` implement the generic `Executor` interface, so it’s very easy to switch from a thread-based to a process-based solution using `concurrent.futures`.

> For simple uses, the only notable difference between the two concrete executor classes is that `ThreadPoolExecutor.__init__ ` requires a `max_workers` argument setting the number of threads in the pool. That is an optional argument in `ProcessPoolExecutor`, and most of the time we don’t use it — _the default is the number of CPUs returned by `os.cpu_count()`_. This makes sense: for CPU bound processing it makes no sense to ask for more workers than CPUs. On the other hand, for I/O bound processing you may use 10, 100 or 1000 threads in a `ThreadPoolExecutor`; the best number depends on what you’re doing and the available memory, and finding the optimal number will require careful testing.
