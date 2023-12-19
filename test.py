def my_gen():
    n=0
    while True:
        yield n
        n += 2
    

gen = my_gen()

for i in range(10):
    print(next(gen))

print("Hello World")

for i in range(10):
    print(next(gen))