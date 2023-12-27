class MyGenerator:
    def __init__(self, init, last):
        self.curr = init
        self.last = last
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr < self.last:
            num = self.curr
            self.curr +=1
            return num
        else:
            raise StopIteration
        
gen = MyGenerator(2,5)

for i in gen:
    print(i)