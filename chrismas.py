#1) Exercise Build christmass tree

for i in range(10):
    spaces = " "*(10-i)
    hashes = "*"*(2*i-1)
    print(spaces + hashes)
for i in range(3):
    print(f'{" "*7}{"#"*5}')


#2) Exercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        duplicates.append(i)
dup = set(duplicates)

print(dup)

#3) Exercise: Make a funstion that prints the highest even

def highest_even(li):
    highest = 0
    for i in li:
        if i>highest and i%2==0:
            highest = i
    return highest

print(highest_even([10,2,3,4,8,11])) 