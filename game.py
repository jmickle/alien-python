from lib.alien import Alien
from lib.city import City
from lib.util import open_data_file, parse_connection
import sys
import argparse


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



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("aliens", type=int, help="Number of Aliens to create")
    parser.add_argument("map_file", help="filename of test data")

    args = parser.parse_args()

    city_data = get_city_data(args.map_file)
    aliens = get_aliens(args.aliens)
    

if __name__ == "__main__":
    sys.exit(main())
