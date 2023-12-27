my_file = open("output.txt", 'r+')
print(my_file.read())
my_file.close()

# or we can do it as

with open('output.txt', 'r+') as my_file:
    print(my_file.read())