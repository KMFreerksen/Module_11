
"""
Program: employee.py
Auther: Katie Freerksen
Last Date Modified: 12/12/2022
This creates an employee class, and puts together a string of the attributes
"""


class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, lname, fname, addy='', phone=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if not phone_number_characters.issuperset(phone):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone = phone

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, addy):
        self.address = addy

    def set_phone(self, phone):
        self.phone = phone

    def display(self):
        return self.last_name + ", " + self.first_name + "\n" + self.address + "\n" + self.phone + "\n"
