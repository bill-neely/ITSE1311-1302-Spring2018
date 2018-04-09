import bowling

def displayGame(bowlingGame):
    print ''
    print 'Player: ' + bowlingGame.playerName
    print ''
    print 'Frame1 | Frame2 | Frame3 | Frame4 | Frame5 | Frame6 | Frame7 | Frame8 | Frame9 | Frame10'
    frames = ''
    for frame in bowlingGame.frames:
        if len(frame.rolls) == 1:
            frames += '  ' + str(frame.rolls[0]) + '   | '
        elif len(frame.rolls) == 2:
            frames += ' ' + str(frame.rolls[0]) + ', ' + str(frame.rolls[1]) + '  | '
        elif len(frame.rolls) == 3:
            frames += str(frame.rolls[0]) + ', ' + str(frame.rolls[1]) + ', ' + str(frame.rolls[2])
    print frames
    print 'Final Score: ' + str(bowlingGame.finalScore())


playerName = raw_input("Please enter the player's name: ")
game = bowling.Bowling(playerName)

while not game.gameOver:
    pins = raw_input('Frame: ' + str(game.currentFrame().frameNumber) + ' Roll: ' + str(game.currentFrame().rollNumber) + ' How many pins? ')
    if not game.addRoll(int(pins)):
        print 'Invalid number of pins. Try Again.'

displayGame(game)
