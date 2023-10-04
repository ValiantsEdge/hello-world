import random

class pokemon():
    def __init__(self, name, gen):
        self.name = name
        self.gen = gen
    
    def __str__(self):
        return self.name + " is from Gen " + self.gen

mons = {"Staraptor":"Gen 4",
"Hoopa":"Gen 6"}
mons1 = list(mons.items())
randommon = random.choice(mons1)
print(randommon)
