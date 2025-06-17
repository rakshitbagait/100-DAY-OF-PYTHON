def decorator_fun(function):
    def wrapper_function():
        function()
    return wrapper_function

def say_hello():
    
    print("hello")
say_hello()