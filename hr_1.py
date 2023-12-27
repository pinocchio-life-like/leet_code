name_ = []
max_ = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        name_.append(name)
        max_.append(score)
    
indices = []
for i in range(0, len(max_)):
    if max[i] == max_[1]:
        indices.append(max_[i])
    
print(indices)