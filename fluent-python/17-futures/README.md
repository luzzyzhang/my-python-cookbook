# Examples: Web download in three style
> `flags.py` runs sequentially: it onley requests the next image when the previous one is downloaded and saved to disk.
> `flags_threadpool.py`, `flags_asyncio.py` make concurrent downloads: they request all images practically at the same time, and save the files as they arrive.
> The `flags_threadpool.py` uses the `concurrent.futures` package, while `flags_asyncio.py` uses `asyncio`.
