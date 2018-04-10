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
