class SuperList(list):
    def __len__(self):
        return 1000
    
list1  = SuperList((1,2,3,4,5))

print(len(list1))