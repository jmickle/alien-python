import random

class Alien:
    def __init__(self, name, trapped, current_city, steps = 0):
        self.name = name
        self.alive = True
        self.trapped = trapped
        self.steps = steps
        self.current_city = current_city

    def travel_list(self):
        list = ['N','S','E','W']
        random.shuffle(list)
        return list

    def die(self):
        self.alive = False

    def move_city(self, new_city):
        self.current_city = new_city
        self.steps += 1
