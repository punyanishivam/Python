# Map, filter and reduce
#map_filter_reduce(func_or_lambda, iterable)

# Map - Apply a function to all elements in an iterable
items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x **3), items))
print(a)

# Filter - Filter out values on a specific condition from an iterable
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))

# Reduce - Reduce the list to a result
from functools import reduce
a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a)
