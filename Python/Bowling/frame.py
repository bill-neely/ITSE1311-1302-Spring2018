class Frame:

    def __init__(self, frameNumber):
        self.frameNumber = frameNumber
        self.rollNumber = 1
        self.rolls = []
        self.rollsRemainInFrame = 2
        self.inExtraRolls = False
        self.pinsRemainInFrame = 10
        self.frameOver = False

    def addRoll(self, pins):
        if not self.frameOver and pins <= self.pinsRemainInFrame:
            self.rolls.append(pins)
            self.pinsRemainInFrame -= pins
            self.rollsRemainInFrame -= 1
            self.rollNumber += 1
            if (self.pinsRemainInFrame <= 0 or self.rollsRemainInFrame <= 0):
                if self.frameNumber != 10 or self.inExtraRolls:
                    self.pinsRemainInFrame = 0
                    self.frameOver = True
                else:
                    if self.isStrike():
                        self.inExtraRolls = True
                        self.pinsRemainInFrame = 20
                        self.rollsRemainInFrame = 2
                    elif self.isSpare():
                        self.inExtraRolls = True
                        self.pinsRemainInFrame = 10
                        self.rollsRemainInFrame = 1
                    else:
                        self.pinsRemainInFrame = 0
                        self.frameOver = True
            return True
        return False

    def isSpare(self):
        if self.frameNumber != 10:
            return (len(self.rolls) == 2 and sum(self.rolls) == 10)
        else:
            return (len(self.rolls) >= 2 and (self.rolls[0] + self.rolls[1]) == 10)

    def isStrike(self):
        if self.frameNumber != 10:
            return (len(self.rolls) == 1 and sum(self.rolls) == 10)
        else:
            return (len(self.rolls) >= 1 and self.rolls[0] == 10)
        return False
