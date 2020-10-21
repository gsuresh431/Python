def square(x):
    return x*x

def my_map(func, args_list):
    result = []
    for x in args_list:
        result.append(square(x))
    return result

print(square(3))
print(my_map(square, [1,2,3,4,5]))