def selfDividingNumbers(left, right):
    result = []
    for num in range(left, right+1):
        if isSelfDividing(num):
            result.append(num)
    return result

def isSelfDividing(num):
    digits = [int(digit) for digit in str(num)]
    for digit in digits:
        if digit == 0 or num % digit != 0:
            return False
    return True
