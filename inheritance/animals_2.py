#!/usr/bin/env python3

# python inheritance

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumber(self):
        print("This animal is sleeping")

# additional actions
class Burrowing:
    def burrow(self):
        print("This animal is burrowing")

class Aquatic:
    def breathe_underwater(self):
        print("This animal can breath underwater")

class Aerial:
    def navigate(self):
        print("This animal is navigating in the air")
# subclasses
class Rabit(Animal, Burrowing):
    def run(self):
        print("This rabit is eating")

class Fish(Animal, Aquatic):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal, Aerial):
    def fly(self):
        print("This hawk is flying")

rab = Rabit()
rab.burrow()

fish = Fish()
fish.breathe_underwater()

hawk = Hawk()
hawk.navigate()
