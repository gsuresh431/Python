# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay 

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    def __str__(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Soumya", "Ranjan", 100)
print(emp1.email)
# emp1.first = "newfirst"
print(emp1.email)