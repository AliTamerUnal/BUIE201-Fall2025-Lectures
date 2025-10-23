class Student:
    def __init__(self, g, n):
        self.grade = g
        self.name = n

    def Study(self):
        print (self.name + ' is studying')

Students = [Student(1.0, "tamer"), ## implicitly calls __init__(address of the new object being created)
                Student(2.0, "ayse"),
                Student(3.0, "fatma")]

for st in Students:
    print (st.grade)

for st in Students:
    st.Study()


