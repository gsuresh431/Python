def decorator_function(original_func):
    
    def wrapper_function():
        print ("wrapper function executed this before original function")
        return original_func()
    
    return wrapper_function

# def display():
#     print("Hello")
# decorated_display = decorator_function(display)
# decorated_display()

# the above is the equivalent of the below code snippet - more pythonic way of decorator things
@decorator_function
def display():
    print("Hello")
display()