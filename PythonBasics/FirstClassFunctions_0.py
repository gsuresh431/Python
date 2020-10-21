def show():
    print("Hello World")

func_var = show
print(type(show))     #<class 'function'>
print(type(func_var)) #<class 'function'>
print(show)     #<function show at 0x000001C48B7203A8>
print(func_var) #<function show at 0x000001C48B7203A8>
show()     #Hello World
func_var() #Hello World