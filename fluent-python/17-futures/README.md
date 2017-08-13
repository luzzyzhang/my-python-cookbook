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
>     The `concurrent.futures` examples are limited by the **`GIL`**, and the `flags_asyncio.py` is _single-threaded_.

