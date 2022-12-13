from Classes.SalariedEmployee import SalariedEmployee
from Classes.person import person

class Manager(person, SalariedEmployee):
    def __init__(self, lname, fname, pay, start, dept, reports=[]):
        super(Manager, self).__init__(lname, fname)
        self.salary = pay
        self.start_date = start
        self.department = dept
        self.direct_reports = reports

    def display(self):
        return self.last_name + ', ' + self.first_name + '\n' + self.start_date + '\n' + "${:.2f}".format(self.salary) + "\n" + self.department + '\n'


#Driver
HomeManager = Manager('Freerksen', 'Katie', 40000, '12/12/2022', 'IT Helpdesk')
print(HomeManager.display())
emp1 = SalariedEmployee('Roger', 'Roy', '', '', 22000, '1/1/2000')
emp2 = SalariedEmployee('Cooper', 'Gary', '', '', 20000, '1/1/2010')
emp3 = SalariedEmployee('Wayne', 'John', '', '', 35000, '1/1/2015')
HomeManager.direct_reports.append(emp1)
HomeManager.direct_reports.append(emp2)
HomeManager.direct_reports.append(emp3)
for SalariedEmployee in HomeManager.direct_reports:
    print(SalariedEmployee.display())
HomeManager.salary = 42000
print(HomeManager.display())
