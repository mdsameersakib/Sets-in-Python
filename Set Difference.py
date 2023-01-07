.difference()

The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

>>> s = set([1,2,3,4,5])
>>> print(s.difference([1,2,3]))
{4,5}


>>> s = set("University")
>>> print(s.difference("versity"))
{'U', 'n'}


>>> s = set("University")
>>> print(s - set("versity"))
{'U', 'n'}
