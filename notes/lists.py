# NS 1st 

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("after calling the function")
    return wrapper

@decorator
def greet():
    print("hello, world ")

greet()

@decorator
def add():
    print(1+1)


add()