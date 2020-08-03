import random
from wumpus_logic import *


def initalize_data(width, height, cell_size):
    pits = []
    visible = []
    breeze = []
    stench = []
    for i in range(width*height):
        stench.append(False)
        breeze.append(False)
        pits.append(False)
        visible.append(False)
    for i in range(10):
        index = random.randint(0, width*height-1)
        pits[index] = True
    data = [width, height, cell_size, pits, visible, width-1, height-1, int(width/2), int(height/2), False, True, True, 0, 0, stench, breeze]
    return data


def setDimensions(data, width, height):
    data[0] = width
    data[1] = height


def getDimensions(data):
    return [data[0], data[1]]


def setCellSize(data, cell_size):
    data[2] = cell_size


def getCellSize(data):
    return data[2]


def setBreeze(data, x, y):
    [width, height] = getDimensions(data)
    i = y * width + x
    data[15][i] = True


def getBreeze(data, x, y):
    [width, height] = getDimensions(data)
    i = y * width + x
    return data[15][i]


def iToXY(data, i):
    [width, height] = getDimensions(data)
    x = i % width
    y = 1 + (int(i / width))
    return [x, y]


def setPits(data, pits):
    data[3] = pits
    for i in pits:
        if pits[i]:
            if cellIsInCavern(data, iToXY(data, i)[0] + 1, iToXY(data, i)[1]):
                setBreeze(data, iToXY(data, i)[0] + 1, iToXY(data, i)[1])
            elif cellIsInCavern(data, iToXY(data, i)[0] - 1, iToXY(data, i)[1]):
                setBreeze(data, iToXY(data, i)[0] - 1, iToXY(data, i)[1])
            elif cellIsInCavern(data, iToXY(data, i)[0], iToXY(data, i)[1] + 1):
                setBreeze(data, iToXY(data, i)[0], iToXY(data, i)[1] + 1)
            elif cellIsInCavern(data, iToXY(data, i)[0], iToXY(data, i)[1] - 1):
                setBreeze(data, iToXY(data, i)[0], iToXY(data, i)[1] - 1)


def getPits(data):
    return data[3]


def setVisible(data, visible):
    data[4] = visible


def getVisible(data):
    return data[4]


def getWumpusPosition(data):
    return [data[5], data[6]]


def setGoldPosition(data, gold_x, gold_y):
    data[7] = gold_x
    data[8] = gold_y


def getGoldPosition(data):
    return [data[7], data[8]]


def setHaveGold(data, have_gold):
    data[9] = have_gold


def getHaveGold(data):
    return data[9]


def setIsAlive(data, is_Alive):
    data[11] = is_Alive


def getIsAlive(data):
    return data[11]


def setAdventurerPosition(data, adventurer_x, adventurer_y):
    data[12] = adventurer_x
    data[13] = adventurer_y


def getAdventurerPosition(data):
    return [data[12],data[13]]


def getStench(data, x, y):
    [width, height] = getDimensions(data)
    i = y * width + x
    return data[14][i]


def setStench(data, stench_x, stench_y):
    [width, height] = getDimensions(data)
    i = stench_y * width + stench_x
    data[14][i] = True


def setWumpusPosition(data, wumpus_x, wumpus_y):
    data[5] = wumpus_x
    data[6] = wumpus_y
    if cellIsInCavern(data, wumpus_x + 1, wumpus_y):
        setStench(data, wumpus_x + 1, wumpus_y)
    elif cellIsInCavern(data, wumpus_x - 1, wumpus_y):
        setStench(data, wumpus_x - 1, wumpus_y)
    elif cellIsInCavern(data, wumpus_x, wumpus_y + 1):
        setStench(data, wumpus_x, wumpus_y + 1)
    elif cellIsInCavern(data, wumpus_x, wumpus_y - 1):
        setStench(data, wumpus_x, wumpus_y - 1)