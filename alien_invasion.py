from lib.alien import Alien
from lib.city import City
from lib.game import start_game
import sys
import argparse
import random


def open_data_file(file):
    '''
      params:
        - file: string

      description:
        Takes a file location and opens the file for parsing then reads the cites into a dict

      return:
        dict

    '''
    with open(file, 'r') as data_file:
        cities = {}

        cities_list = data_file.readlines()

        for city in cities_list:
            city_data = city.split()
            city_name = city_data.pop(0)
            cities[city_name] = city_data
        return cities


def parse_connection(connection):
    '''
      params:
        - connection: string

      description:
        takes a connection string and splits it and parses it into a standard direction

      return:
        direction: string
        city: string

    '''
    conns = connection.split('=')

    original_direction = conns.pop(0)
    city = conns.pop()

    direction = ''

    if original_direction == 'north':
        direction = 'N'
    elif original_direction == 'south':
        direction = 'S'
    elif original_direction == 'west':
        direction = 'W'
    elif original_direction == 'east':
        direction = 'E'

    return direction, city


def get_city_data(map_file):
    '''
      params:
        - map_file: string

      description:
        Takes a file location and opens the file for parsing then reads the connections into a list.

      return:
        dict

    '''
    city_data = open_data_file(map_file)
    city_dict = {}
    for city in city_data:
        city_dict[city] = City(city)

    for city, connections in city_data.items():

        for connection in connections:
            dir, neighbor = parse_connection(connection)
            neighbor_city = city_dict[neighbor]
            # print(neighbor_city.__dict__)
            city_dict[city].add_neighbor(dir, neighbor_city)

    return city_dict


def get_aliens(num_aliens):
    return [Alien("a-{0}".format(str(x)), False, None)
            for x in range(num_aliens)]


def assign_aliens(city_data, aliens):
    '''
      params:
        - citydata: dict
        - aliens: list

      description:
        Takes a dictionary of city data and assigns aliens to the city.

      return:
        None

    '''
    for alien in aliens:
        city_name, cityobj = random.choice(list(city_data.items()))
        alien.move_city(cityobj)
        cityobj.alien_entrance(alien)


def main():
    '''
       Main Function
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("aliens", type=int, help="Number of Aliens to create")
    parser.add_argument("map_file", help="filename of test data")

    args = parser.parse_args()

    city_data = get_city_data(args.map_file)
    aliens = get_aliens(args.aliens)

    #print city_data
    assign_aliens(city_data, aliens)

    start_game(city_data, aliens)


if __name__ == "__main__":
    sys.exit(main())
