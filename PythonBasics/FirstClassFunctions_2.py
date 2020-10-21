'''
First class functions:
    - Being ablt to assign function to a variable
    - Being able to pass function as argument to another functions
    - Being able to return a function from within a function - code below
'''

def logger(msg):

    def local_logger():
        print('Log:', msg)
    
    return local_logger

log_hi = logger('Hi')
print(log_hi)
log_hi()

log_hello = logger('Hello')
print(log_hello)
log_hello()

# Example#2

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    
    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)
print(print_h1('wonderful'))
