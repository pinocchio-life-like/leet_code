class FibGenerator:
    first = 0
    second = 1
    curr = 0
    def __init__(self, index):
        self.index = index
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < FibGenerator.curr:
            raise StopIteration
        else:
            FibGenerator.curr +=1
            temp = FibGenerator.first
            FibGenerator.first = FibGenerator.second
            FibGenerator.second = temp + FibGenerator.second
            return temp
     
fib = FibGenerator(10)

for i in fib:
    print(i)  