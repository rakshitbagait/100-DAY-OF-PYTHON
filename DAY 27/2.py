class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
dog =Animal("tiger","bark")
print(dog.name)

class Car:
    def __init__(self,**kw):
        self.company = kw["company"]
        self.model =kw["model"]

my_car =Car(company ="nissan",model="model")
print(my_car.company)
        
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)