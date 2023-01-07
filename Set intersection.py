.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

>>> s = set([1,2,3])
>>> print(s.intersection([1,2,3,4,5]))
{1,2,3}

>>> s = set("versity")
>>> print(s.intersection("University"))
{'e', 's', 'i', 'r', 'v', 't', 'y'}

>>> s = set("Brac")
>>> print(s & set("University"))
{'r'}
