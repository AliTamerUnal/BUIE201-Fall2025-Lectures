import student

class Lecture:
    def __init__(self, code):
        self._code = code
        self._students = []
        self._addStudent(student.Student("tamer", 6.00))

    def addStudent(self, s: student.Student):
        self._students.append(s)