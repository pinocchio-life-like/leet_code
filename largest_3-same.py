def maxGoodNum(num):
    max_num = ""
    for i in range(len(num) - 2):
        substr = num[i:i + 3]
        if substr[0] == substr[1] == substr[2] and substr > max_num:
            max_num = substr
    return max_num