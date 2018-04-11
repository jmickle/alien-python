class City():

    def __init__(
            self,
            name,
            aliens=[],
            destroyed=False,
            north=None,
            south=None,
            east=None,
            west=None):
        self.name = name
        self.aliens = aliens
        self.destroyed = destroyed
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def add_neighbor(self, direction, neighbor):
        '''
          params:
            - direction: string
            - neighbor: obj

          description:
            Takes a direction and assigns the neighbor object to it

          return:
            None

        '''
        if direction == 'N':
            self.north = neighbor
        elif direction == 'S':
            self.south = neighbor
        elif direction == 'E':
            self.east = neighbor
        elif direction == 'W':
            self.west = neighbor

    def destroy(self):
        '''
          description:
            sets destroyed status true

          return:
            None

        '''
        self.destroyed = True

    def travel_spots(self, direction):
        '''
          params:
            - direction: string

          description:
            Takes a direction and checks if it is a valid travel location

          return:
            bool

        '''
        neighbor = None

        if direction == 'N':
            neighbor = self.north
        elif direction == 'S':
            neighbor = self.south
        elif direction == 'E':
            neighbor = self.east
        elif direction == 'W':
            neighbor = self.west

        # print(neighbor)
        if neighbor and not neighbor.destroyed:
            return True
        else:
            return False

    def get_neighbor(self, direction):
        '''
          params:
            - direction: string

          description:
            Takes a direction and returns the neighbor

          return:
            obj

        '''
        if direction == 'N':
            return self.north
        elif direction == 'S':
            return self.south
        elif direction == 'E':
            return self.east
        elif direction == 'W':
            return self.west

    def alien_entrance(self, alien):
        '''
          params:
            - alien: obj

          description:
            Takes an alien and assigns them to a city

          return:
            None

        '''
        self.aliens.append(alien)

    def alien_exit(self, alien):
        '''
          params:
            - alien: obj

          description:
            removes an alien from a city

          return:
            None

        '''
        try:
            index = self.aliens.index(alien)
            self.aliens.pop(index)
        except BaseException:
            print("Alien not in {0}".format(self.name))

    def get_aliens(self):
        '''
          description:
            returns list of aliens

          return:
            list of obj

        '''
        return ", ".join([alien.name for alien in self.aliens])

    def get_city_info(self):
        '''
          description:
            prints the city data to out

        '''
        city_sum = self.name

        if(self.travel_spots('N')):
            city_sum += " north={0}".format(self.north.name)

        if(self.travel_spots('S')):
            city_sum += " south={0}".format(self.south.name)
        if(self.travel_spots('E')):
            city_sum += " east={0}".format(self.east.name)
        if(self.travel_spots('W')):
            city_sum += " west={0}".format(self.west.name)

        return city_sum
