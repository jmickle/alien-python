class City():

    def __init__(self, name, aliens = [], destroyed = False, north = None, south = None, east= None, west=None):
        self.name = name
        self.aliens = aliens
        self.destroyed = destroyed
        self.north = north
        self.south = south
        self.east = east
        self.west = west


    def add_neighbor(self, direction, neighbor):
        if direction == 'N':
            self.north = neighbor
        elif direction == 'S':
            self.south = neighbor
        elif direction == 'E':
            self.east = neighbor
        elif direction == 'W':
            self.west = neighbor

    def destroy(self):
        self.destroyed = True

    def travel_spots(self, direction):
        neighbor = None

        if direction == 'N':
            neighbor = self.north
        elif direction == 'S':
            neighbor = self.south
        elif direction == 'E':
            neighbor = self.east
        elif direction == 'W':
            neighbor = self.west

        if neighbor and not neighbor.destroyed:
            return True
        else:
            return False

    def get_neighbor(self, direction):
        if direction == 'N':
            return self.north
        elif direction == 'S':
            return self.south
        elif direction == 'E':
            return self.east
        elif direction == 'W':
            return self.west

    def alien_entrance(self, alien):
        self.aliens.append(alien)

    def alien_exit(self, alien):
        try:
            index = self.aliens.index(alien)
            self.aliens.pop(index)
        except:
            print("Alien not in {0}".format(self.name))

    def get_aliens(self):
        return ", ".join([alien.name for alien in self.aliens])

    def get_city_info(self):
        city_sum = self.name

        if(self.can_travel('N')):
            city_sum += " north={0}".format(self.north.name)

        if(self.can_travel('S')):
            city_sum += " south={0}".format(self.south.name)
        if(self.can_travel('E')):
            city_sum += " east={0}".format(self.east.name)
        if(self.can_travel('W')):
            city_sum += " west={0}".format(self.west.name)

        return city_sum
