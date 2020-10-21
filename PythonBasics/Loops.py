dummy = ['Once', 'upon', 'a', 'time']
enum_obj = enumerate(dummy) 
print(type(enum_obj)) #<class 'enumerate'>
for index, value in enumerate(dummy):
    print(f"{index}:{value}")