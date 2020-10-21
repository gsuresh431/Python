'''
*args, **kwargs allow us to accept an arbitrary number of arguments

'''

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Maths', 'Art', name="Jon", age=45 )
# ('Maths', 'Art')
# {'name': 'Jon', 'age': 45}
# SO, we see that
# - args is a tuple with all positional arguments
# - kwargs is a dictionary with all keyword value


# * and ** have different meaning when used while invoking functions 
courses = ['Maths', 'Art']
info = {'name':'Jon', 'age':45}
student_info(*courses, **info)
# ('Maths', 'Art')
# {'name': 'Jon', 'age': 45}
# So, we see that
# - *courses actually UNPACKS the list
# - **info also UNPACKS the dict
# So, essentially the call becomes student_info('Maths', 'Art', name='Jon', age='45')
