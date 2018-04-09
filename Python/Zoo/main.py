import repository

myZoo = repository.makeTheZoo()
visitorName = raw_input('Welcome to ' + myZoo.name + '. What is your name? ')

while myZoo.stillActive:
    print ''
    print 'Your current location is: ' + myZoo.currentLocation.name
    if myZoo.currentLocation.animal is not None:
        print ' Animal: ' + myZoo.currentLocation.animal.name
        print '  You can ask:'
        print '    Sounds'
        print '    Food'
        print '    Shelter'
    else:
        print ' There is no animal here.'
    print ' From here, you can go: '
    for direction, locationID in myZoo.currentLocation.neighbors.items():
        print '  ' + direction + ' to ' + myZoo.locations[locationID].name
    if myZoo.currentLocation.allowExit:
        print '  Exit to the Parking Lot'
    stayHere = True
    while stayHere:
        print
        choice = raw_input('What would you like to do ' + visitorName + '? ')
        print ''
        if choice in myZoo.currentLocation.neighbors.keys():
            myZoo.changeLocation(choice)
            stayHere = False
        elif choice.lower() == 'exit':
            myZoo.exit()
            stayHere = False
        elif choice.lower() == 'sounds':
            print myZoo.currentLocation.animal.speak()
        elif choice.lower() == 'food':
            print myZoo.currentLocation.animal.diet()
        elif choice.lower() == 'shelter':
            print myZoo.currentLocation.animal.shelter()

print ''
print 'Thank you for visiting.  Come again.'
