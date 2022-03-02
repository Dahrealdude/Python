class Employee:
    def __init__(self,first, last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + ' @company.com '

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey','Shaer',50000)
emp_2 = Employee('David', 'Johnson', 60000)


print(emp_1.first, emp_1.last, emp_1.pay)
#print(emp_2.email,)


# print(emp_1.fullname())


