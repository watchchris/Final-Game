import pygame
import simpleGE
import random

class Money(simpleGE.Sprite):
    def __init__(self, Scene):
        super().__init__(Scene)
        self.setImage("Money.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Purple(simpleGE.Sprite):
    def __init__(self, Scene):
        super().__init__(Scene)
        self.setImage("Purple.png")
        self.setSize(25, 25)
        self.minSpeed = 7
        self.maxSpeed = 8
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        self.reset()

    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)


    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Chris(simpleGE.Sprite):
    def __init__(self, Scene):
        super().__init__(Scene)
        self.setImage("Chris.png")
        self.setSize(100, 100)
        self.position = (320, 400)
        self.moveSpeed = self.scene.moveSpeed
        self.scene = Scene

    def process(self):
        moveSpeed = self.scene.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed


class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)


class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 10"
        self.center = (500, 30)


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()

        self.setImage("skyLine.jpg")

        self.soundMoney = simpleGE.Sound("pickupCoin.wav")
        self.numMoneys = 10

        self.soundPurple = simpleGE.Sound("powerUp.wav")
        self.numPurples = 1

        self.score = 0
        self.lblScore = LblScore()

        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.lblTime = LblTime()

        self.moveSpeed = 5
        self.chris = Chris(self)

        self.chris = Chris(self)

        self.Moneys = []
        for i in range(self.numMoneys):
            self.Moneys.append(Money(self))

        self.purple = []
        for i in range(self.numPurples):
            self.purple.append(Purple(self))

        self.sprites = [self.chris,
                        self.Moneys,
                        self.lblScore,
                        self.lblTime,
                        self.purple]

    def process(self):
        for money in self.Moneys:
            if money.collidesWith(self.chris):
                money.reset()
                self.soundMoney.play()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"

        for purple in self.purple:
            if purple.collidesWith(self.chris):
                purple.reset()
                self.soundPurple.play()
                self.chris.moveSpeed = (self.moveSpeed + 10)
                if self.moveSpeed > 10:
                    keepGoing = True
                    while self.moveSpeed > 10:
                        if self.timer.totalTime() - 10:
                            keepGoing = False



        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()


class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()

        self.prevScore = prevScore

        self.setImage("skyLine.jpg")
        self.response = "Quit"

        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "You are Chris.",
            "A Cybersecurity student at Ball State.",
            "Move with left and right arrow keys.",
            "Catch as much money as you can",
            "Purple coins will give you",
            "a much needed speed boost.",
            "",
            "Good Luck!"]

        self.directions.center = (320, 200)
        self.directions.size = (500, 250)

        self.buttonPlay = simpleGE.Button()
        self.buttonPlay.text = "Play"
        self.buttonPlay.center = (100, 400)

        self.buttonQuit = simpleGE.Button()
        self.buttonQuit.text = "Quit"
        self.buttonQuit.center = (540, 400)

        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (320, 400)

        self.lblScore.text = f"Last score: {self.prevScore}"

        self.sprites = [self.directions,
                        self.buttonPlay,
                        self.buttonQuit,
                        self.lblScore]

    def process(self):
        if self.buttonPlay.clicked:
            self.response = "Play"
            self.stop()

        if self.buttonQuit.clicked:
            self.response = "Quit"
            self.stop()


def main():
    keepGoing = True
    lastScore = 0

    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()

        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score

        else:
            keepGoing = False


if __name__ == "__main__":
    main()