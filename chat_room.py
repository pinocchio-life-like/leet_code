def check_hello(word):
    hello = "hello"
    i = 0
    for char in word:
        if char == hello[i]:
            i += 1
            if i == len(hello):
                return "YES"
    return "NO"

# Test the function
word = input()
result = check_hello(word)
print(result)
