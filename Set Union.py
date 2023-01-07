.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

>>> s = set([1,2,3])
>>> print(s.union([1,2,3,4,5]))
{1,2,3,4,5}

>>> s = set("BRAC")
>>> print(s.union("University))
{'A', 'e', 'U', 'v', 's', 'B', 'y', 'R', 'n', 't', 'C', 'r', 'i'}


>>> s = set("BRAC")
>>> print(s|set("University"))
{'A', 'v', 's', 'y', 'e', 'U', 'r', 'n', 'i', 'R', 't', 'B', 'C'}
