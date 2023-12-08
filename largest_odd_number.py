def largestOddNumber(num):
    if int(num)%2 > 0 or int(num[-1])%2>0:
       return num
    if int(num[-1])%2 == 0:
        return largestOddNumber(num[1:])

    large = 0

    for i in num:
        if int(i) > large and int(i)%2 > 0:
            large = int(i)
    return "" if large == 0 else str(large)
    
    
    
print(largestOddNumber("10133890"))

def largestOddNumber(num):
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""
