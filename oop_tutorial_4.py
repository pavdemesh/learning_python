# SOURCE: https://www.youtube.com/watch?v=JeznW_7DlB0

class Person:
    num_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return Person.num_people

    @classmethod
    def add_person(cls):
        cls.num_people += 1


class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")


p1 = Person("Mike")
p2 = Person("Jim")
p3 = Person("Jenn")
print(Person.number_of_people())
print(Person.num_people)

print(Math.add5(8))
Math.pr()
