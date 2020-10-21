class Employee:
    
    raise_amount = 1.04 
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
   

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emps(self):

        for emp in self.employees:
            print ("-->",emp.email)


dev1 = Developer("Test", "Developer1", 200, 'Perl')
dev2 = Developer("Test", "Developer2", 300, 'Python')

mgr1 = Manager("Poli","Bala",900, [dev1])
mgr1.add_emp(dev2)
print(mgr1.fullname())
mgr1.show_emps()

