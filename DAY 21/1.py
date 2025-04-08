class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("inhale","exhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("swim")
    def breathe(self):
        super().breathe()
        print("through gills")
nemo=Fish()
nemo.swim()
nemo.breathe()