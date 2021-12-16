
class Employee:
    def __init__ (self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def give_raise(self, pay_raise = 5000): # function that is only dealing with changing the values of the that class
        self.pay_raise = pay_raise
        self.salary += pay_raise

# employee = Employee("Andy", "Mimbs", 50000)
# employee.give_raise(10000)
# print(employee.salary)


