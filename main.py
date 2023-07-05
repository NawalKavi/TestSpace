# Importing library and initialising.
from pygame import *
import random

ylol = random.randint(1, 69)
if ylol == 69:
    while ylol == 69:
        print("seggsee")
init()

# Setting up the screen.
width = 1200
height = 700
mainWindow = display.set_mode((width, height))

# Images.
imageDictionary = {
    "invader1": transform.scale(image.load("Images//Invader 1.png"), (40, 40)),
    "invader2": transform.scale(image.load("Images//Invader 2.png"), (40, 40)),
    "invader3": transform.scale(image.load("Images//Invader 3.png"), (40, 40)),
    "player": transform.scale(image.load("Images//Player.png"), (40, 40))
}

invaderArray = []


class Object():
    def __init__(self, objectName, sizeX, sizeY):
        self.Size = [sizeX, sizeY]
        self.CentrePosition = [sizeX / 2, sizeY / 2]
        self.AbsolutePosition = [0, 0]
        self.ObjectName = objectName

    def editPosition(self, newX, newY):
        self.AbsolutePosition[0] = newX - self.Size[0] / 2
        self.AbsolutePosition[1] = newY - self.Size[1] / 2
        self.CentrePosition[0] = newX
        self.CentrePosition[1] = newY


class Invader(Object):
    def __init__(self, objectName, sizeX, sizeY, invaderType):
        self.invaderType = invaderType
        super().__init__(objectName, 5, 20)
        invaderArray.append(self)


def generateInvader():
    for row in range(0, 6):
        for column in range(0, 17):
            newInvader = Invader("Invader", 40, 40, "invader1")
            newInvader.editPosition((column + 1) * 40, 75 + (row + 1) * 40)


# Game loop.
oneSecondTick = 0
gameRunning = True

generateInvader()
print(invaderArray)
while gameRunning == True:
    for gameEvent in event.get():
        # Quits the game by closing the window.
        if gameEvent.type == QUIT:
            gameRunning = False
        # Handles keyboard actions.
        if gameEvent.type == KEYDOWN:
            if gameEvent.key == K_UP:
                pass

    # Fills the window with the specified colour (black).
    mainWindow.fill((0, 0, 0))

    for invaderValue in invaderArray:
        mainWindow.blit(imageDictionary[invaderValue.invaderType],
                        (invaderValue.AbsolutePosition[0], invaderValue.AbsolutePosition[1]))

    # Game fps.
    time.Clock().tick(144)

    # Displays the output.
    display.flip()