# SOURCE: https://www.youtube.com/watch?v=JeznW_7DlB0

class Dog:

    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age
        print(f"You just created an object with name {self.dog_name} and age of {self.dog_age}")

    def get_age(self):
        return self.dog_age
    
    def bark_multi(self, x):
        print("bark " * x)


d = Dog("Timka", 34)
d.bark_multi(5)
print(f"The age is {d.get_age()}")
