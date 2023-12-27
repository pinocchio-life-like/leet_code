# Squaring a list using lambda expressions
my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

# Sorting a list using lamda expression 
unsorted = [(0,2), (4,3), (9,9), (10,-1)]

unsorted.sort(key = lambda item: item[1])
print(unsorted)