class Zoo:
    def __init__(self, name, locations):
        self.name = name
        self.stillActive = True
        self.locations = locations
        self.currentLocation = self.locations[1]

    def changeLocation(self, direction):
        neighborID = self.currentLocation.neighbors[direction]
        self.currentLocation = self.locations[neighborID]

    def exit(self):
        if self.currentLocation.allowExit:
            self.stillActive = False

class Location:
    def __init__(self, id, name, animal, neighbors, allowExit):
        self.id = id
        self.name = name
        self.animal = animal
        self.neighbors = neighbors
        self.allowExit = allowExit

class Animal:
    def __init__(self, name, soundMade, foodEaten, shelterType):
        self.name = name
        self.soundMade = soundMade
        self.foodEaten = foodEaten
        self.shelterType = shelterType

    def speak(self):
        return 'The ' + self.name + ' sounds like: ' + self.soundMade

    def diet(self):
        return 'The ' + self.name + ' eats ' + self.foodEaten

    def shelter(self):
        return 'The ' + self.name + ' prefers: ' + self.shelterType
