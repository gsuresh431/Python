class Employee:
    
    raise_amount = 1.04 
    no_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first, self.last)
        Employee.no_of_emps += 1

    def fullname(self):
        print ("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay *= self.raise_amount
    
    # @classmethod    
    # - @classmethod is a DECORATOR 
    # - It tells that the following def is a class method(not a regular or static method)
    # - The first argument to classmethod is always the class instance itself
    # - This is similar to regular methods where the first arg is self (the object itself)
    # - By conventions, we name the first argument of a classmethod as cls - which denotes the class instance

    @classmethod
    def string_to_instance(cls, string):
        # This is an example where classmethod is used as ALTERNATE Constructor
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @classmethod
    def set_raise_amount(cls, amount):
        # This is an example of classmethod where it simply behaves on an attribute in class instance
        # As obvious, this will change the value in the class namespace only
        # It will have no effect on the object namespace
        cls.raise_amount = amount

    # @staticmethod
    # - its a decorator which tells the following def is a static method(not a class method or regular method)
    # -    classmethod: first arg = class itself  = cls
    # - regular method: first arg = object itself = self
    # -  static method: no mandatory/default arguments - Its just like regular functions  

    @staticmethod
    def is_working_day(day):
        if ( day.weekday()==5  or day.weekday()==6):
            return False
        return True

# Creating a new object via @classmethod
emp_3 = Employee.string_to_instance("Soumya-Das-20000")

# Changing the value of class attribute via @classmethod
print(Employee.__dict__) #'raise_amount': 1.04,
Employee.set_raise_amount(1.05)
print(Employee.__dict__) #'raise_amount': 1.05,

