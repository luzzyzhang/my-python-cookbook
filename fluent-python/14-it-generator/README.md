## iterable

	```
		Any object from which the iter built-in function can obtain an iterator.
        Objects implementing an __iter__ method returning an iterator are iterable.
        Sequences are always iterable;
        so as are objects implementing a __getitem__ method which takes 0-based indexes.
	```

## iterator

	```
        Any object that implements the __next__ no-argument method
        which returns the next item in a series or raises StopIteration
        when there are no more items.
        Python iterators also implement the __iter__ method so they are iterable as well.
	```
