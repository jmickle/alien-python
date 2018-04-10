from lib.alien import Alien
from lib.city import City
import sys
import argparse
import random


def open_data_file(file):
    with open(file, 'r') as data_file:
        cities = {}

        cities_list = data_file.readlines()

        for city in cities_list:
            city_data = city.split()
            city_name = city_data.pop(0)
            cities[city_name] = city_data

        return cities

def parse_connection(connection):
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
    city_data = open_data_file(map_file)
    city_dict = {}
    for city in city_data:
        city_dict[city] = City(city)

    for city, connections in city_data.items():

        for connection in connections:
            dir, neighbor = parse_connection(connection)
            neighbor_city = city_dict[neighbor]
            city_dict[city].add_neighbor(dir, neighbor)

    return city_dict

def get_aliens(num_aliens):
    return [Alien("a-{0}".format(str(x)), False, None) for x in xrange(num_aliens)]

def assign_aliens(city_data, aliens):
    for alien in aliens:
        city_name, cityobj = random.choice(list(city_data.items()))
        alien.move_city(cityobj)
        cityobj.alien_entrance(alien)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("aliens", type=int, help="Number of Aliens to create")
    parser.add_argument("map_file", help="filename of test data")

    args = parser.parse_args()

    city_data = get_city_data(args.map_file)
    aliens = get_aliens(args.aliens)

    #print city_data
    assign_aliens(city_data, aliens)


if __name__ == "__main__":
    sys.exit(main())
