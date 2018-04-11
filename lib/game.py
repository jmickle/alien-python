
def game_status(aliens):

    alive_aliens = [ alien for alien in aliens if alien.alive and not alien.trapped ]
    fresh_aliens = [ alien for alien in alive_aliens if alien.steps < 10000 ]

    if len(alive_aliens) == 0 or len(fresh_aliens) == 0:
        return False
    else:
        return True

def start_game(city_data, aliens):

    while(game_status(aliens)):
        for city_name, city in city_data.items():
            if not city.destroyed:
                for alien in city.aliens:
                    if alien.alive and not alien.trapped:
                        tmp = False
                        test = alien.travel_list()
                        #print(alien.travel_list())
                        for location in alien.travel_list():
                            if city.travel_spots(location):
                                new_location = city.get_neighbor(location)
                                alien.move_city(location)
                                city.alien_exit(alien)
                                new_location.alien_entrance(alien)
                                tmp = False
                                break
                            else:
                                tmp = True

                        if tmp:
                            alien.trapped = True

        for city_name, city in city_data.items():
            if not city.destroyed and len(city.aliens) > 1:
                for alien in city.aliens:
                    alien.die()

                dead_aliens = city.get_aliens()
                print("{0} aliens died in a stand off, {1} was destroyed!".format(dead_aliens, city.name))

    for city_name, city in city_data.items():
        if not city.destroyed:
            print(city.get_city_info())
