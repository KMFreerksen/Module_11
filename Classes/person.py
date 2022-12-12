from Classes.address import address

class person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + str(self.address.display())

# Driver
addy1 = address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
person1 = person('Hammer', 'Martin', addy1)
print(person1.display())
# apartemnt number is at the end. Why?
addy2 = address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
person2 = person('Hammer', 'Martin', addy2)
print(person2.display())
del(addy1, addy2)
del(person1, person2)
