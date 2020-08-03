import random
from wumpus_logic import *
from wumpus_data import *

data = initalize_data(5, 5, 0)
move = 0

while not getHaveGold(data) or getIsAlive(data):

    move += 1
    path = random.randint(0, 4)
    [adventurer_x, adventurer_y] = getAdventurerPosition(data)
    print("> move: " + str(move) + ", x: " + str(adventurer_x) + " y: " +str(adventurer_y))
    if path == 1:
        print("> willing to turn right ...")
        if cellIsInCavern(data, adventurer_x + 1, adventurer_y):
            if cellIsSafe(data, adventurer_x, adventurer_y):
                print("> safe cell --> any cell")
                visitCell(data, adventurer_x + 1, adventurer_y)
                setAdventurerPosition(data, adventurer_x + 1, adventurer_y)
            else:
                if cellIsVisible(data, adventurer_x + 1, adventurer_y) or cellIsSafe(data, adventurer_x + 1, adventurer_y):
                    print("> smelly cell --> safe cell.")
                    visitCell(data, adventurer_x + 1, adventurer_y)
                    setAdventurerPosition(data, adventurer_x + 1, adventurer_y)
                elif not cellIsVisible(data, adventurer_x + 1, adventurer_y):
                    print("> smelly cell --> not visited cell: یا بخت یا اقبال")
                    choice = random.choice[True, False]
                    if choice:
                        visitCell(data, adventurer_x + 1, adventurer_y)
                        setAdventurerPosition(data, adventurer_x + 1, adventurer_y)
    elif path == 2:
        print("> willing to turn left ...")
        if cellIsInCavern(data, adventurer_x - 1, adventurer_y):
            if cellIsSafe(data, adventurer_x, adventurer_y):
                print("> safe cell --> any cell")
                visitCell(data, adventurer_x - 1, adventurer_y)
                setAdventurerPosition(data, adventurer_x - 1, adventurer_y)
            else:
                if cellIsVisible(data, adventurer_x - 1, adventurer_y) or cellIsSafe(data, adventurer_x - 1, adventurer_y):
                    print("> smelly cell --> safe cell.")
                    visitCell(data, adventurer_x - 1, adventurer_y)
                    setAdventurerPosition(data, adventurer_x - 1, adventurer_y)
                elif not cellIsVisible(data, adventurer_x - 1, adventurer_y):
                    print("> smelly cell --> not visited cell: یا بخت یا اقبال")
                    choice = random.choice[True, False]
                    if choice:
                        visitCell(data, adventurer_x - 1, adventurer_y)
                        setAdventurerPosition(data, adventurer_x - 1, adventurer_y)

    elif path == 3:
        print("> willing to go down ...")
        if cellIsInCavern(data, adventurer_x, adventurer_y + 1):
            if cellIsSafe(data, adventurer_x, adventurer_y):
                print("> safe cell --> any cell")
                visitCell(data, adventurer_x, adventurer_y + 1)
                setAdventurerPosition(data, adventurer_x, adventurer_y + 1)
            else:
                if cellIsVisible(data, adventurer_x, adventurer_y + 1) or cellIsSafe(data, adventurer_x, adventurer_y + 1):
                    print("> smelly cell --> safe cell.")
                    visitCell(data, adventurer_x, adventurer_y + 1)
                    setAdventurerPosition(data, adventurer_x, adventurer_y + 1)
                elif not cellIsVisible(data, adventurer_x, adventurer_y + 1):
                    print("> smelly cell --> not visited cell: یا بخت یا اقبال")
                    choice = random.choice[True, False]
                    if choice:
                        visitCell(data, adventurer_x, adventurer_y + 1)
                        setAdventurerPosition(data, adventurer_x, adventurer_y + 1)

    elif path == 4:
        print("> willing to go up ...")
        if cellIsInCavern(data, adventurer_x, adventurer_y - 1):
            if cellIsSafe(data, adventurer_x, adventurer_y):
                print("> safe cell --> any cell")
                visitCell(data, adventurer_x, adventurer_y - 1)
                setAdventurerPosition(data, adventurer_x, adventurer_y - 1)
            else:
                if cellIsVisible(data, adventurer_x, adventurer_y - 1) or cellIsSafe(data, adventurer_x, adventurer_y - 1):
                    print("> smelly cell --> safe cell.")
                    visitCell(data, adventurer_x, adventurer_y - 1)
                    setAdventurerPosition(data, adventurer_x, adventurer_y - 1)
                elif not cellIsVisible(data, adventurer_x, adventurer_y - 1):
                    print("> smelly cell --> not visited cell: یا بخت یا اقبال")
                    choice = random.choice[True, False]
                    if choice:
                        visitCell(data, adventurer_x, adventurer_y - 1)
                        setAdventurerPosition(data, adventurer_x, adventurer_y - 1)

if getHaveGold(data) == True:
    print("you won!!")
    print("adventurer position: " + "(" + str(data[12]) + ", " + str(data[13]) + ")")
    if getGoldPosition(data) == [data[12], data[13]]:
        print("cell contains gold: True")

else:
    print("you died!")
    print("adventurer position: " + str(data[12]) + str(data[13]))
    print("cell contains pit: " + str(cellContainsPit(data, data[12], data[13])))
    print("cell contains wumpus: " + str(cellContainsWumpus(data, data[12], data[13])))