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
  |itertools|`compress(it, selector_it)`|consumes two iterables in parallel; yields items from it whenever the corresponding item inselector_itis truthy|
  |(built-in)|`filter(predicate, it)`|appliespredicateto each item ofiterable, yielding the item if predicate(item) is truthy; if predicate is None, only truthy items are yielded|
  |itertools|`filterfalse(predicate, it)`|same as filter, with the predicate logic negated: yields items whenever predicate computes falsy|
  |itertools|`islice(it, stop)` or `islice(it, start, stop, step=1)`|yields items from a slice of it, similar tos[:stop] or s[start:stop:step] except it can be any iterable, and the operation is lazy|
  |itertools|`takewhile(predicate, it)`|yields items while predicate computes truthy, then stops and no further checks are made|
  |itertools|`tropwhile(predicate, it)`|consumes it skipping items while predicate computes truthy, then yields every remaining item (no further checks are made)|

### Mapping generator functions

|module|function|description|
|---|---|---|
|itertools|`accumulate(it,[func])`| yields accumulated sums; if func is provided, yields the result of applying it the first pair of items, then to the first result and next item etc.|
|(built-in)|`enumerate(iterable,start=0)`| yields 2-tuples of the form (index, item), where index is counted from start, and item is taken from the iterable|
|(built-in)|`map(func, it1, [it2, ..., itN])`| appliesfuncto each item ofit, yielding the result; if N iterables are given,func must take N arguments and the iterables will be consumed in parallel|
|itertools|`starmap(func, it)`|appliesfuncto each item ofit, yielding the result; the input iterable should yield iterable items iit, and func is applied as `func(*iit)`|
    
    
```python
>>> import operator
>>> import itertools
>>> list(itertools.starmap(operator.mul, enumerate('abcdefg', 1)))
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg']
```

### Generator functions that merge multiple input iterables.

|module|function|description|
|---|---|--|
|itertools|`chain(it1, ..., itN)`|yield all items fromit1, then fromit2etc., seamlessly|
|itertools|`chain.from_iterable(it)`|yield all items from each iterable produced byit, one after the other,seamlessly;itshould yield iterable items, for example, a list of iterables|
|itertools|`product(it1, ..., itN, repeat=1)`|cartesian product: yields N-tuples made by combining items from each input iterable like nestedforloops could produce;repeatallows the input iterables to be consumed more than once|
|(built-in)|`zip(it1, ..., itN)`|yields N-tuples built from items taken from the iterables in parallel, silently stopping when the first iterable is exhausted|
|itertools|`zip_longest(it1, ..., itN, fillvalue=None)`|yields N-tuples built from items taken from the iterables in parallel, stopping only when the last iterable is exhausted, filling the blanks with the fillvalue|



### Generator functions that expand each input item into multiple output items.

|module|function|description|
|---|---|---|
|itertools|`combinations(it, out_len)`|yield combinations ofout_lenitems from the items yielded byit|
|itertools|`combinations_with_replacement(it, out_len)||
|itertools|`count(start=0, step=1)`|yield combinations ofout_lenitems from the items yielded byit,
including combinations with repeated items.|
|itertools|`permutations(it, out_len=None)`|yields numbers starting atstart, incremented bystep, indefinitely
yields items fromitstoring a copy of each, then yields the entire sequence repeatedly, indefinitely|
|itertools|`repeat(item, [times])`|yield permutations ofout_lenitems from the items yielded byit; by default,out_lenislen(list(it))|

### Rearranging generator functions
