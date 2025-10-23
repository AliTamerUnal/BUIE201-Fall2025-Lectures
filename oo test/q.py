"""
Add necessary code before the indicated line so that `Run()` function returns the following string as output:

This family has 3 men and 2 women members. Ages of the children are 10 12 15

All your code should be written as classes in accordance with object-oriented principles. Use polymorphism as much as possible.

# Your code will be inserted before this line.

def Run():
	Family = FAMILY()
    M = MOTHER() 
    F = FATHER()
	S1 = SON(10)
    D = DAUGHTER(12) 
    S2 = SON(15)
    Family.AddMember(M)
    Family.AddMember(F)
    Family.AddMember(S1)
    Family.AddMember(D)
    Family.AddMember(S2)
	Family.Print()

print(Run())

"""

class Person:
    def __init__(self, age=None):
        self._age = age

    def IncrementManCount(self, counter):
        pass

    def IncrementWomanCount(self, counter):
        pass

    def CollectChildrenAges(self, age_list):
        pass


class MOTHER(Person):
    def IncrementWomanCount(self, counter):
        counter[0] += 1


class FATHER(Person):
    def IncrementManCount(self, counter):
        counter[0] += 1


class Child(Person):
    def __init__(self, age):
        super().__init__(age)

    def CollectChildrenAges(self, age_list):
        age_list.append(str(self._age))


class SON(Child):
    def __init__(self, age):
        super().__init__(age)

    def IncrementManCount(self, counter):
        counter[0] += 1


class DAUGHTER(Child):
    def __init__(self, age):
        super().__init__(age)

    def IncrementWomanCount(self, counter):
        counter[0] += 1


class FAMILY:
    def __init__(self):
        self._members = []

    def AddMember(self, person: Person):
        self._members.append(person)

    def Print(self):
        men = [0]
        women = [0]
        children_ages = []
        for member in self._members:
            member.IncrementManCount(men)
            member.IncrementWomanCount(women)
            member.CollectChildrenAges(children_ages)

        print(f"This family has {men[0]} men and {women[0]} women members. Ages of the children are {' '.join(children_ages)}")

def Run():
	Family = FAMILY()
	M = MOTHER() 
	F = FATHER()
	S1 = SON(10)
	D = DAUGHTER(12) 
	S2 = SON(15)
	Family.AddMember(M)
	Family.AddMember(F)
	Family.AddMember(S1)
	Family.AddMember(D)
	Family.AddMember(S2)
	Family.Print()

Run()