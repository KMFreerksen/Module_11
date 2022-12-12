from Classes.person import person
from Classes.address import address
import numpy


class student:
    """Student class using class Person, class Address, and Class Composition"""
    def __init__(self, person, major, start, gpa):
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        float_range = numpy.linspace(0,4,400)
        if not (major_characters.issuperset(major)):
            raise ValueError
        if not (isinstance(gpa, (float)) and float_range.__contains__(gpa)):
            raise ValueError
        self.person = person
        self.major = major
        self.start_date = start
        self.gpa = gpa

    def change_major(self, new_major):
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-! ")
        if not (major_characters.issuperset(new_major)):
            raise ValueError
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return str(self.person.display() + "\n Start Date: " + self.start_date + "\n Major: " + self.major + "\n GPA: " + str(self.gpa) + "\n")


#Driver
addy1 = address('3210', 'NE 44th', 'Ave', 'Des Moines', 'Iowa', '50317')
person1 = person('Freerksen', 'Katie', addy1)
myself = student(person1, 'CIS', 'Jan 2022', 4.0)
print(myself.display())
myself.change_major('Being Awesome!')
myself.update_gpa(3.0)
print(myself.display())
del (addy1, person1, myself)
