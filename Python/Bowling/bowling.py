import frame

class Bowling:
    def __init__(self, playerName):
        self.playerName = playerName
        self.gameOver = False
        self.frames = []
        self.advanceFrame()

    def advanceFrame(self):
        self.frames.append(frame.Frame(len(self.frames) + 1))

    def currentFrame(self):
        return self.frames[-1]

    def addRoll(self, pins):
        if not self.gameOver:
            if self.currentFrame().addRoll(pins):
                if self.currentFrame().frameOver:
                    if self.currentFrame().frameNumber == 10:
                        self.gameOver = True
                    else:
                        self.advanceFrame()
                return True
        return False

    def finalScore(self):
        totalScore = 0
        for frame in self.frames:
            totalScore += sum(frame.rolls)
            if frame.frameNumber != 10:
                if frame.isSpare():
                    totalScore += self.frames[frame.frameNumber].rolls[0]
                if frame.isStrike():
                    totalScore += self.frames[frame.frameNumber].rolls[0]
                    if len(self.frames[frame.frameNumber].rolls) > 1:
                        totalScore += self.frames[frame.frameNumber].rolls[1]
                    else:
                        totalScore += self.frames[frame.frameNumber + 1].rolls[0]
        return totalScore
