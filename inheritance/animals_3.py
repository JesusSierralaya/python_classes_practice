#!/usr/bin/env python3

# python inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal name {self.name} has been created")

# additional actions
class Burrowing:
    def __init__(self, burrow_depth):
        self.burrow_depth = burrow_depth
        print(f"Burrow ability with depth {self.burrow_depth} added")

# subclasses
class Rabit(Animal, Burrowing):
    def __init__(self, name, burrow_depth, speed):
        super().__init__(name)
        # Animal.__init__(self, name)
        Burrowing.__init__(self, burrow_depth)
        self.speed = speed
        print(f"Rabit with speed {self.speed} has been created")

    def run(self):
        print(f"This rabit named {self.name} is running at speed {self.speed}")

rabit = Rabit("Thumper", 5,20)
