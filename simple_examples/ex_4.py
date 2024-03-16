#!/usr/bin/env python3

class Robot:
    def __init__(self, name):
        self.name = name
    def introduceSelf(self):
        print(f"Hi! My name is {self.name}.")

r1 = Robot("Tom")
r2 = Robot("Jerry")

r1.introduceSelf()

class Person:
    def __init__(self, name, personality, is_sitting, robot_owned):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = robot_owned

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggresive", True, r2)
p2 = Person("Becky", "talkative", False, r1)

print(p1.is_sitting)
p1.stand_up()
print(p1.is_sitting)

p1.robot_owned.introduceSelf()
