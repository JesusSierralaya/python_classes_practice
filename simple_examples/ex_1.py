#!/usr/bin/env python3

# class
class Person:
    def __init__(self, age, weight, name):
        self.age = age
        self.weight = weight
        self.name = name
    # first attribute
    def learn(self):
        print("Learning...")

# set an instance
user = Person(35, 80, "Jesus")

# print instance data
print(user.name)
user.learn()
