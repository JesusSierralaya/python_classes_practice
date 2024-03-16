#!/usr/bin/env python3

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduceSelf(self):
        print(f"Hello! My name is {self.name}, my color is {self.color} and my weight is {self.weight} pounds.")

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

# r1.introduceSelf()
# r2.introduceSelf()
r1.model = "old"

print(f"my model is {r1.model}")

class Robot2:
    def introduceSelf(self):
        print("Hello! My name is " + self.name)

# r3 = Robot("Chester", "Brown", 5)
r3 = Robot2()
r3.name = "Chester"
r3.model = "new"

r3.introduceSelf()
print(f"my model is {r3.model}")
