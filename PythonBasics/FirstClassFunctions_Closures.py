def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    
    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

print(hi_func)    #<function outer_func.<locals>.inner_func at 0x000002346827B3A8>
print(hello_func) #<function outer_func.<locals>.inner_func at 0x0000024E99B9BC18>

print(hi_func.__name__)    #inner_func
print(hello_func.__name__) #inner_func
hi_func()    #hi
hello_func() #hello

    