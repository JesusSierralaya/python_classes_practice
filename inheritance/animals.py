#!/usr/bin/env python3

# python inheritance

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def slumber(self):
        print("This animal is sleeping")

class Rabit(Animal):
    def run(self):
        print("This rabit is eating")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rab = Rabit()
print(rab.alive)

fish = Fish()
fish.eat()

hawk = Hawk()
hawk.fly()
