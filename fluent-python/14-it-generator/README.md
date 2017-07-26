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
    which returns the next item in a series or raises StopIteration when there are no more items.
    Python iterators also implement the __iter__ method so they are iterable as well.
```

## Generator functions in standard library

### Filtering generator functions

|module|function|description|
  |---|---|---|
  |itertools|compress(it, selector_it)|consumes two iterables in parallel; yields items from it whenever the corresponding item inselector_itis truthy|
  |(built-in)|filter(predicate, it)|appliespredicateto each item ofiterable, yielding the item if predicate(item) is truthy; if predicate is None, only truthy items are yielded|
  |itertools|filterfalse(predicate, it)|same as filter, with the predicate logic negated: yields items whenever predicate computes falsy|
  |itertools|islice(it, stop) or islice(it, start, stop, step=1)|yields items from a slice of it, similar tos[:stop]or s[start:stop:step] except it can be any iterable, and the operation is lazy|
  |itertools|takewhile(predi cate, it)|yields items whilepredicatecomputes truthy, then stops and no further checks are made|

### Mapping generator functions

### Generator functions that merge multiple input iterables.

### Generator functions that expand each input item into multiple output items.

### Rearranging generator functions
