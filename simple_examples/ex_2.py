#!/usr/bin/env python3

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def double_speed(self):
        self.speed *= 2

warrior = Character(100, 50, 10)
ninja = Character(80, 40, 40)
print(f'The warrior speed is {warrior.speed}')
print(f'The ninja speed is {ninja.speed}')
warrior.double_speed()
print(f'The warrior speed is {warrior.speed}')
print(f'The ninja speed is {ninja.speed}')
