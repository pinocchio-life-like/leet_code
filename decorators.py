def decorator(func):
    def wrapper_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")
    return wrapper_func

@decorator
def hello_func(*args, **kwargs):
    print(*args)
    
hello_func("Helloooo") 