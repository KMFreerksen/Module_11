from Classes.person import person


class student (person):
    """Student derived class of Person base class"""
    def __init__(self, student_id, lname, fname, major='Computer Science', gpa=0.0):
        super(student, self).__init__(lname, fname)
        self._major = major
        self._gpa = gpa
        self._student_id = student_id

    def display(self):
        return self.last_name + ', ' + self.first_name +':(' + str(self._student_id) + ') ' + self._major + ' gpa: ' + str(self._gpa)

# Driver
my_student = student(900111111, 'Song', 'River')
print(my_student.display())
my_student = student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
