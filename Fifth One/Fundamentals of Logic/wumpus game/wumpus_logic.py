from wumpus_data import *
  

def cellContainsWumpus(data, x, y):
    if getWumpusPosition(data) == [x,y]:
        return True
    else:
        return False


def cellContainsGold(data, x, y):
    if getGoldPosition(data) == [x,y]:
        return True
    else:
        return False


def cellContainsPit(data, x, y):
    [width, height] = getDimensions(data)
    pits = getPits(data)
    i = y * width + x
    return pits[i]


def cellIsVisible(data, x, y):
    [width, height] = getDimensions(data)
    i = y * width + x
    if getVisible(data)[i]:
        return True
    else:
        return False


def cellIsInCavern(data, x, y):
    if x >= 0 and y >= 0 and x < data[0] and y < data[1]:
        return True
    else:
        print("> cell not available /")
        return False


def cellIsSafe(data, x, y):
    if getBreeze(data, x, y) or getStench(data, x, y):
        return False
    else:
        return True


def neighbourCellIsVisible(data, x, y):
    if cellIsInCavern(data, x + 1, y) and cellIsVisible(data, x + 1, y):
        return True
    elif cellIsInCavern(data, x - 1, y) and cellIsVisible(data, x - 1, y):
        return True
    elif cellIsInCavern(data, x, y + 1) and cellIsVisible(data, x, y + 1):
        return True
    elif cellIsInCavern(data, x, y - 1) and cellIsVisible(data, x, y - 1):
        return True

    return False


def neighbourCellContainsPit(data, x, y):
    if cellIsInCavern(data, x + 1, y) and cellContainsPit(data, x + 1, y):
        return True
    elif cellIsInCavern(data, x - 1, y) and cellContainsPit(data, x - 1, y):
        return True
    elif cellIsInCavern(data, x, y + 1) and cellContainsPit(data, x, y + 1):
        return True
    elif cellIsInCavern(data, x, y - 1) and cellContainsPit(data, x, y - 1):
        return True

    return False


def neighbourCellContainsWumpus(data, x, y):
    if cellIsInCavern(data, x + 1, y) and cellContainsWumpus(data, x + 1, y):
        return True
    elif cellIsInCavern(data, x - 1, y) and cellContainsWumpus(data, x - 1, y):
        return True
    elif cellIsInCavern(data, x, y + 1) and cellContainsWumpus(data, x, y + 1):
        return True
    elif cellIsInCavern(data, x, y - 1) and cellContainsWumpus(data, x, y - 1):
        return True

    return False


def setCellVisible(data, x, y):
    [width, height] = getDimensions(data)
    visible = getVisible(data)
    i = y * width + x
    visible[i] = True
    setVisible(data, visible)


def visitCell(data, x, y):
    if cellContainsPit(data, x, y) or cellContainsWumpus(data, x, y):
        setIsAlive(data, False)
    elif cellContainsGold(data, x, y):
        setHaveGold(data, True)
    setCellVisible(data, x, y)
