
def isPalindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        return str(x) == str(x)[::-1]

