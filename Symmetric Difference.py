.symmetric_difference()

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).


>>> s = set([0,1,2,3])
>>> print(s.symmetric_difference([1,2,3,4,5,6,7]))
{0, 4, 5, 6, 7}

>>> s = set("Myversity")
>>> print(s.symmetric_difference("University"))
{'U', 'n', 'M'}

>>> s = set("Brac")
>>> print(s ^ set("University"))
{'U', 'n', 'M'}
