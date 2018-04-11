import random


class Alien:
    def __init__(self, name, trapped, current_city, steps=0):
        self.name = name
        self.alive = True
        self.trapped = trapped
        self.steps = steps
        self.current_city = current_city

    def travel_list(self):
        '''
          description:
            Provides a random shuffling of directions for the game

        '''
        list = ['N', 'S', 'E', 'W']
        random.shuffle(list)
        return list

    def die(self):
        '''
          description:
            destroy the alien

        '''
        self.alive = False

    def move_city(self, new_city):
        '''
          params:
            - new_city: obj
          description:
            sets an alien to the new city and increases steps


        '''
        self.current_city = new_city
        self.steps += 1
