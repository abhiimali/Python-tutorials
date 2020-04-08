class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

d1=Dog()
d1.walk()
d2=Cat()
d2.walk()

