from Classes.employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, pay, start):
        super().__init__(lname, fname, addy, phone)
        pay_range = range(10000, 200000, 1)
        if not (isinstance(pay, (int,float)) and pay_range.__contains__(pay)):
            raise ValueError
        self.salary = pay
        self.start_date = start

    def give_raise(self, new_pay):
        pay_range = range(10000, 200000, 1)
        if not (isinstance(new_pay, (int,float)) and pay_range.__contains__(new_pay)):
            raise ValueError
        self.salary = new_pay

    def display(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\n" + self.phone + "\n" + "${:.2f}".format(self.salary) + "\n" + self.start_date + "\n"


#driver
ceo = SalariedEmployee('Freerksen', 'Katie', '123 Main St, Ankeny, IA 50023', '515-555-5555', 40000, '12/12/2022')
print(ceo.display())
ceo.give_raise(45000)
print(ceo.display())
del ceo
