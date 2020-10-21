x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        # nonlocal x # outer x
        # global x # global x
        x = 'inner x'
        print(x)
        
    print(x)
    inner()

print(x)
outer()
print(x)