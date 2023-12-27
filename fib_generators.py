def fib(index):
    init = 0
    last = 1
    for i in range(index):
        yield init
        temp = init
        init = last
        last = temp + last


for i in fib(10):
    print(i)