import zoo

def makeTheZoo():
    return zoo.Zoo("Bill's Wonderland Zoo", getLocations())

def getLocations():
    locations = {}
    locations.update(one())
    locations.update(two())
    locations.update(three())
    locations.update(four())
    locations.update(five())
    locations.update(six())
    locations.update(seven())
    locations.update(eight())
    locations.update(nine())
    return locations

def one():
    id = 1
    name = 'Entrance'
    animal = None
    neighbors = {}
    neighbors['s'] = 9
    neighbors['sw'] = 2
    neighbors['se'] = 8
    allowExit = True
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def two():
    id = 2
    name = 'Africa Live'
    animal = zoo.Animal('Lion', 'roar', 'whatever it wants', 'dry, arid land')
    neighbors = {}
    neighbors['ne'] = 1
    neighbors['se'] = 9
    neighbors['s'] = 3
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def three():
    id = 3
    name = 'Antarctica'
    animal = zoo.Animal('Penguin', 'silence', 'fish', 'cold air with lots of water')
    neighbors = {}
    neighbors['n'] = 2
    neighbors['e'] = 9
    neighbors['s'] = 4
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def four():
    id = 4
    name = 'Bird House'
    animal = zoo.Animal('Maquaw', 'squawk, squawk', 'nuts, berries, insects', 'clean crisp air')
    neighbors = {}
    neighbors['n'] = 3
    neighbors['e'] = 5
    neighbors['ne'] = 9
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def five():
    id = 5
    name = 'Elbonia'
    animal = zoo.Animal('Hippophant', 'Moo', 'humans, unicorns', 'filthy water, with bugs in it')
    neighbors = {}
    neighbors['n'] = 9
    neighbors['e'] = 4
    neighbors['w'] = 6
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def six():
    id = 6
    name = 'Enchanted Wood'
    animal = zoo.Animal('Unicorn', 'Giggle Snort', 'magic seeds, magic grass, imaginary leaves', 'forest full of people who will believe anything')
    neighbors = {}
    neighbors['n'] = 7
    neighbors['w'] = 5
    neighbors['nw'] = 9
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def seven():
    id = 7
    name = 'Deep Sea'
    animal = zoo.Animal('Sea Serpent', 'ssssssss', 'you', 'salt water, preferably 1000 meters deep')
    neighbors = {}
    neighbors['s'] = 6
    neighbors['n'] = 8
    neighbors['w'] = 9
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def eight():
    id = 8
    name = 'Cave Land'
    animal = zoo.Animal('Dragon', 'roaring growl', 'farm animals, humans, other dragons', 'dark caves, with water, and one entrance')
    neighbors = {}
    neighbors['nw'] = 1
    neighbors['sw'] = 9
    neighbors['s'] = 7
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}

def nine():
    id = 9
    name = 'Aquarium'
    animal = zoo.Animal('Seal', 'barking', 'fish and penguins', 'water with some dry land')
    neighbors = {}
    neighbors['n'] = 1
    neighbors['nw'] = 2
    neighbors['ne'] = 8
    neighbors['w'] = 3
    neighbors['e'] = 7
    neighbors['sw'] = 4
    neighbors['se'] = 6
    neighbors['s'] = 5
    allowExit = False
    return {id : zoo.Location(id, name, animal, neighbors, allowExit)}
