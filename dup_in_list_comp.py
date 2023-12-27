some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({dup for dup in some_list if some_list.count(dup) > 1})
print(duplicates)


# BTW: A Higher Order Function is a function that accepts 
# another function as a parameter or return a function as
# a return value 