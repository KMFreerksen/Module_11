from Classes.employee import Employee
import numpy


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, pay, start):
        super().__init__(lname, fname, addy, phone)
        pay_range = numpy.linspace(7, 30, 2300)
        self.hourly_pay = pay
        self.start_date = start

    def give_raise(self, new_pay):
        pay_range = numpy.linspace(7.25, 30, 2275)
        self.hourly_pay = new_pay

    def display(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\n" + self.phone + "\n" + "${:.2f}".format(self.hourly_pay) + "\n" + self.start_date + "\n"

#driver
developer = HourlyEmployee('Freerksen', 'Katie', '123 Main St, Ankeny, IA 50023', '515-555-5555', 10.00, '12/12/2022')
print(developer.display())
developer.give_raise(12.00)
print(developer.display())
del developer
