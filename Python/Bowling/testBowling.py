import bowling
import frame
import sys

def testCorrectNumberOfRolls(testName, frameNumber, rolls, expectedNumberOfRolls):
    aFrame = frame.Frame(frameNumber)
    for roll in rolls:
        allowed = aFrame.addRoll(roll)
    if len(aFrame.rolls) == expectedNumberOfRolls:
        print('PASS: ' + testName)
    else:
        print('FAIL: ' + testName + ' expected ' + str(expectedNumberOfRolls) + ' but got ' + str(len(aFrame.rolls)))

testCorrectNumberOfRolls("Allow two in frame 1", 1, [2, 3], 2)
testCorrectNumberOfRolls("Strike ends frame 1, test 1", 1, [10], 1)
testCorrectNumberOfRolls("Strike ends frame 1, test 2", 1, [10, 1], 1)
testCorrectNumberOfRolls("Two in frame 10", 10, [1, 1], 2)
testCorrectNumberOfRolls("Frame 10 spare/strike", 10, [1, 9, 10], 3)
testCorrectNumberOfRolls("Frame 10 strike + 2", 10, [10, 1, 9], 3)
testCorrectNumberOfRolls("Frame 10 strike + strike + strike", 10, [10, 1, 9], 3)
testCorrectNumberOfRolls("Frame 10 stop at 3", 10, [10, 10, 10, 10], 3)
testCorrectNumberOfRolls("Frame 10 stop at 3, two", 10, [10, 0, 0, 0], 3)

def testIsSpare(testName, frameNumber, rolls, expectedSpare):
    aFrame = frame.Frame(frameNumber)
    for roll in rolls:
        aFrame.addRoll(roll)
    if aFrame.isSpare() == expectedSpare:
        print('PASS: ' + testName)
    else:
        print('FAIL: ' + testName + ' expected ' + str(expectedSpare) + ' but got ' + str(aFrame.isSpare()))

testIsSpare("Not a spare - Frame 1", 1, [2,3], False)
testIsSpare("Is not a spare - Frame 7", 7, [10], False)
testIsSpare("Is a spare - Frame 9", 9, [1,9], True)
testIsSpare("Not a spare - Frame 10", 10, [2,3], False)
testIsSpare("Not a spare - Frame 10", 10, [10, 1, 9], False)
testIsSpare("Not a spare - Frame 10", 10, [10, 10, 10], False)
testIsSpare("Is a spare - Frame 10", 10, [3, 7, 1], True)

def testIsStrike(testName, frameNumber, rolls, expectedStrike):
    aFrame = frame.Frame(frameNumber)
    for roll in rolls:
        aFrame.addRoll(roll)
    if aFrame.isStrike() == expectedStrike:
        print('PASS: ' + testName)
    else:
        print('FAIL: ' + testName + ' expected ' + str(expectedStrike) + ' but got ' + str(aFrame.isStrike()))

testIsStrike("Not a strike - Frame 1", 1, [2,3], False)
testIsStrike("Not a strike - Frame 1", 1, [1,9], False)
testIsStrike("Is a strike - Frame 1", 1, [10], True)
testIsStrike("Is not a strike - Frame 10", 10, [1, 9, 10], False)
testIsStrike("Is a strike - Frame 10", 10, [10, 1, 1], True)
testIsStrike("Is a strike - Frame 10", 10, [10, 1, 9], True)
testIsStrike("Is a strike - Frame 10", 10, [10, 10, 10], True)


def testFinalScore(testName, rolls, expectedScore):
    aGame = bowling.Bowling(testName)
    for roll in rolls:
        aGame.addRoll(roll)
    if aGame.finalScore() == expectedScore:
        print('PASS: ' + testName)
    else:
        print('FAIL: ' + testName + ' expected ' + str(expectedScore) + ' but got ' + str(aGame.finalScore()))


game1rolls = [4,3, 6,2, 4,2, 8,1, 4,5, 6,2, 7,2, 9,0, 0,5, 6,3]
testFinalScore("Game1FinalScore", game1rolls, 79)

game2rolls = [4,6, 6,2, 4,2, 8,1, 10, 10, 7,3, 9,0, 0,5, 6,4,5]
testFinalScore("Game2FinalScore", game2rolls, 134)

game3rolls = [4,6, 6,2, 4,2, 8,2, 10, 10, 9,1, 9,0, 0,5, 6,4,7]
testFinalScore("Game3FinalScore", game3rolls, 149)

game4rolls = [9,1, 9,1, 9,1, 1,9, 8,2, 9,1, 7,3, 6,4, 5,5, 1,9,10]
testFinalScore("Game4FinalScore", game4rolls, 165)

game5rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,10,10]
testFinalScore("Game5FinalScore", game5rolls, 300)

game6rolls = [9,1, 9,1, 9,1, 1,9, 8,2, 9,1, 7,3, 6,4, 5,5, 10,1,1]
testFinalScore("Game6FinalScore", game6rolls, 166)

game7rolls = [9,1, 9,1, 9,1, 1,9, 8,2, 9,1, 7,3, 6,4, 5,5, 1,3]
testFinalScore("Game7FinalScore", game7rolls, 149)
