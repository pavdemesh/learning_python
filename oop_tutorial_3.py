# https://www.youtube.com/watch?v=JeznW_7DlB0
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Tim", 23)
p.show()
c = Cat("Mirka", 1, "brown")
c.show()
c.speak()
f = Fish("Billy", 22)
f.show()
f.speak()
