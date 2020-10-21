class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)
        
    def fullname(self):
        return "{} {}".format(self.first, self.last) 

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}-{}-{}".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first) + len(self.last)
    
emp1 = Employee("Soumya", "Ranjan", 100)
emp2 = Employee("Correy", "Schafer", 900)

print(emp1) #Soumya-Ranjan-100
print(emp2) #Correy-Schafer-900
print(emp1 + emp2) #1000
print(len(emp1))   #12 
