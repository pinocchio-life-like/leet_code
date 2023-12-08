def test(n):
    if n == 5:
        return "Five "
    else:
        return test(n-1) + "Test "


print(test(10))