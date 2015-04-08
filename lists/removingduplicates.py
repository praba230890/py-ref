"""
Python is awesome
"""

"""
References:
http://pansop.com/1014/
http://www.peterbe.com/plog/uniqifiers-benchmark
"""

"""
Removing deplicates in a list
"""

print """
basic way
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = []
for i in a:
    if i not in b:
        b.append(i)
print b


print """
basic cool way
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
for i,j in zip(a, range(len(a))):
    if i not in a[:j]:
        print i


print """
basic cool! way
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = [a[i] for i in range(len(a)) if a[i] not in a[:i]]  
# or # b = [j for i,j in enumerate(a) if j not in a[:i]]
# or just # [b.append(i) for i in a if not b.count(i)]
print b


print """
doing it just because I can do it, way
"""

from collections import OrderedDict
a = [1,2,3,4,5,6,1,2,3,4,5,6]
ord_dict_a = OrderedDict()
for i in a:
    ord_dict_a[i] = "dummy"
print ord_dict_a.keys()


print """
Yes! It's crazy, way
"""

from collections import OrderedDict
a = [1,2,3,4,5,6,1,2,3,4,5,6]
print OrderedDict(zip(a,[1]*len(a))).keys()


print """
yield, way - just for fun!
"""

def clean(a):
    for i in range(len(a)):   # or use enumerate
        if a[i] not in a[:i]:
            yield a[i]

a = [1,2,3,4,5,6,1,2,3,4,5,6]
for i in clean(a):
    print i


print """
simple set way [unordered]
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = list(set(a))
print b


print """
simple set way [ordered]
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = [i for i in set(a)]
print b


print """
list->tuple->set->list [ordered]
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = list(set(tuple(a)))
print b


print """
more with set [ordered]
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
# add_to_set = set().add # some says this line if added will make the program faster as we are bringing the add method from global to local scope
dummy_set = set()
b = [i for i in a if i not in dummy_set and not dummy_set.add(i)]
print b


print """
now with dict way
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = {}.fromkeys(a).keys()
print b


print """
more dict way 
although this method preserves order in some Python implementations, lets consider it unordered for consistency sake.
For more regarding the consistency problem refer: http://docs.python.org/library/stdtypes.html#dict.items
"""

a = [1,2,3,4,5,6,1,2,3,4,5,6]
b = dict(zip(a,a)).keys()
print b

