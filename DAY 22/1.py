class Animal:
    def sound(self):
        print("make sound")
class Dog (Animal):
    def sound(self):
        print("bark")
dog=Dog()
dog.sound()
animal = Animal()
animal.sound()