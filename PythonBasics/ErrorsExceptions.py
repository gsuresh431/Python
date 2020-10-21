'''
Built-In exceptions
    - Exception heirarchy
Raising an exception
    - AssertionError Exception
    - try-except-else-finally 
    - Custom Exception class

The Assertion statement
'''


###################################################################################################
'''
BUILT-IN EXCEPTIONS
- In Python, all exceptions must be instances of a call that device from - BaseException
- In a try statement with an except clause that mentions a particular class, 
  that clause also handles any exception classes derived from that class
- User code can raise built-in exceptions
- Build-in exception classes can be subclassed to define new exceptions
- Programmers are encourangeD to define new exceptions from Exception class or one of it subclasses 
  rather than from BaseException class - refer User-defined Exceptions
  
- When raising/re-raisning an exception, 
    - __context__ is automatially set to the last exception caught
    - if the new exception is not handled, 
      the traceback that is eventually displayed will inlude originating exception and final exception
      
EXCEPTION HEIRARCHY

BaseException
 +-- SystemExit 
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
           
    
    Exception       - Base class for all exceptions
    StopIteration   - Raised when the next() method of an iterator does not point to any object
    SystemExit      - Raised by sys.exit() function
    StandardError   - Base class for all built-in exceptions except StopeIteration and SystemExit
    LookupError            - Base class for all lookup errors    
        IndexError         - index not found in a sequemce
        KeyError           - key not found in a dictionary
    ArithmeticError        - Base class for all errors that occur numeric calculation
        OverflowError      - Raised when a calculation exceeds maximum limit for a numeric type
        ZeroDivisionError  - Raised when division or module by 0 takes place
        FloatingPointError - Raised when a floating point calculation fails    
    EnvironmentError       - Base class for all exceptions that occur outside the python env
    AssertionError         - Raised when assert statement fails
    EOFError               - Raised when there is no input from raw_input() or input() and the end of file is reached
    ImportError            - Raised when an import statement fails
    KeyboardInterrupt      - Raised when the user interrupts the execution - usually by pressing CTRL+C        
    UnboundLocalError      - Raised when trying to access a local variable in a fucntion or method but no value has been assigned    
    IOError                - Raised when an input/ouput operation fails, such as the print statement or open() on a file
    IOError                - Raised for operating system-related errors
    SyntaxError            - error in python syntax
    SystemError            - Raised when the interpreter finds an internal problem, BUT when this error is encountered, the interpreter doesnot exit
    TypeError              - Raised when an operation/function is attempted that is invalid for the specified data type
    ValueError             - Raised when the built-in functions for a data type has valid type of args, but the args have invalid values specified
    RuntimeError           - Raised when the generated error doesnt fall into any category
        NonImplementedError- Raised when an abstract method that needs to be implemented in an inherited class in not actually implemented

- use 'raise' to throw an exception if a condition occurs
- The statement can be complemented with a custom exception
'''
x = 10
y = 0
if x > 5:
    # manually raising a built in exception
    raise ValueException('{} is greater than 5'.format(x)) 

# Traceback (most recent call last):
#   File "<input>", line 4, in <module>
# Exception: 10 is greater than 5


###################################################################################################
'''
THE AssertionError EXCEPTION
- Instead of waiting for a program to creash midway, you can start by "making a assertion" in Python.
  Details on assert stamement towards end section
- We assert that a condition is met
    - If condition = True, then we are good
    - If condition = False, throw an AssertionError exception
'''
import sys
assert('Linux' in sys.platform), 'The code is designed for Linux platforms only'
# Lets run this in windows platform
# Traceback (most recent call last):
#  File "<input>", line 2, in <module>
# AssertionError: This code runs on Linux only.
 
   
###################################################################################################
'''
TRY-EXCEPT-ELSE-FINALLY BLOCKS
- raise allows you to throw an exception at any time.
- assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
- In the try clause, all statements are executed until an exception is encountered.
- except is used to catch and handle the exception(s) that are encountered in the try clause.
- else lets you code sections that should run only when no exceptions are encountered in the try clause.
- finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.

try: 
   Run this code
except:
    Execute this code when there is an exception
else:
    No exceptions? Run this code
finally:
    always run this code
'''
try:
    assert( 100 in range(10))
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as assertion_err:
    print(assertion_err)
except (IOError, ValueError) as e: # Single except for mulitple exceptions
    print(e)
except Exception as e:
    print(e)
else:
    print('This is executed if no exceptions are thrown from try block')    
finally:
    print('This is always executed')

    
###################################################################################################
'''
CUSTOM EXCEPTIONS - EXCEPTION CLASS - revisit
- you may need to write custom exceptions with custom messages
- we can do so by creating a NEW CLASS - which will be derived from the pre-defined Exception class

'''
class CustomError(Exception):
    def __init__ (self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    
try:
    if(2>1):
        raise CustomError('Custom error message')
except CustomError as ce:
    print(ce.data)

    
    
    
# Example2    
# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass
class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
# our main program
# user guesses a number until he/she gets it right
# you need to guess this number
number = 10
while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")


###################################################################################################
'''
ASSERT STATEMENTS 
- AssertionError Exception

- assert statementis a debugging aid that tests a condition.
- It is not a mechanism to handle run-time error 
    - they are not intended for expected error conditions like ' file not found'
- It aids developers to find root cause of a bug quickly
- If the condition is TRUE, 
    - It does nothing and your program just continues to execute
- If the condition is FALSE,
    - it raises an AssertionError exception with an optional error message
    - example below
  
- CAVEAT#1
    - Asserts can be trurned off globally in the python interpreter 
        - with the -0 and -00 command line switches as well as with 
        - PYTHONOPTIMIZE environment variable in CPython
'''
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."

# Lets run this in windows platform
# Traceback (most recent call last):
#  File "<input>", line 2, in <module>
# AssertionError: This code runs on Linux only.

###################################################################################################



