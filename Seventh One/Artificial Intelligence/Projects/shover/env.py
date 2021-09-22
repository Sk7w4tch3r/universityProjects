class State:
    def __init__(self, map):
        self.map_array = map
        self.cost = 0

    def update(self, i, j, direction):
        self.update_map(i, j, direction)
        self.update_score(i, j, direction)

    def update_score(self, i, j, direction):
        ######### EDITABLE SECTION #########
        pass
        # self.cost+=1

        ######### END OF EDITABLE SECTION #########

    def moveBoxes(self, i, j, direction):
    
        if self.map_array[i][j] == 0:
            self.map_array[i][j] = 1
            return ((i, j), True)
        elif self.map_array[i][j] == -2: # rock
            return ((i, j), False)
        elif self.map_array[i][j] == -1: # hole
            return ((i, j), True)
        elif direction == 'right': # and 
            res = self.moveBoxes(i, j+1, direction)
        elif direction == 'left': # and 
            res = self.moveBoxes(i, j-1, direction)
        elif direction == 'up': # and 
            res = self.moveBoxes(i-1, j, direction)
        elif direction == 'down': # and 
            res = self.moveBoxes(i+1, j, direction)
        return res

    def update_map(self, i, j, direction):
        ######### EDITABLE SECTION #########
        action = (i, j, direction)
        if self.validate_action(action):

            
            if   direction == 'right'   :
                if self.map_array[i][j] == 1:
                    location, check = self.moveBoxes(i, j+1, direction)
                    print(location)
                    self.cost += abs(location[1]-j)
                    if check:
                        self.map_array[i][j-1]  = 0
                        self.map_array[i][j]    = 2 
                        self.map_array[-1]   = (i, j)
                else:
                    self.map_array[i][j-1]  = 0
                    self.map_array[i][j]    = 2 

                    self.map_array[-1]   = (i, j)
            elif direction == 'left'    :
                if self.map_array[i][j] == 1:
                    location, check = self.moveBoxes(i, j-1, direction)
                    print(location)
                    self.cost += abs(location[1]-j)
                    if check:
                        self.map_array[i][j+1] = 0
                        self.map_array[i][j] = 2
                        self.map_array[-1]   = (i, j)
                else:
                    self.map_array[i][j+1] = 0
                    self.map_array[i][j] = 2

                    self.map_array[-1]   = (i, j)
            elif direction == 'up'      :
                if self.map_array[i][j] == 1:
                    location, check = self.moveBoxes(i-1, j, direction)
                    print(location)
                    self.cost += abs(i-location[0])
                    if check:
                        self.map_array[i+1][j] = 0
                        self.map_array[i][j] = 2
                        self.map_array[-1]   = (i, j)
                else:
                    self.map_array[i+1][j] = 0
                    self.map_array[i][j] = 2

                    self.map_array[-1]   = (i, j)
            elif direction == 'down'    :
                if self.map_array[i][j] == 1:
                    location, check = self.moveBoxes(i+1, j, direction)
                    print(location)
                    self.cost += abs(i-location[0])
                    if check:
                        self.map_array[i-1][j] = 0
                        self.map_array[i][j] = 2
                        self.map_array[-1]   = (i, j)
                else:
                    self.map_array[i-1][j] = 0
                    self.map_array[i][j] = 2

                    self.map_array[-1]   = (i, j)
        
        ######### END OF EDITABLE SECTION #########

    def validate_action(self, action):
        i, j, direction = action
        # Checks if the direction is valid
        if direction not in ["up", "down", "right", "left"]:
            print("invalid, action name is wrong")
            return False

        # Makes sure if the coordinates are within range
        if i > len(self.map_array)-1 or j > len(self.map_array[0]):
            print("invalid, chosen coordinate out of border")
            return False

        # Makes sure if it's chosen a box
        # if self.map_array[i][j] != 1:
        #     print("invalid, no box in this slot")
        #     return True

        return True


class Env:
    def __init__(self, map):
        self.state= State(map)

    def take_action(self, action):
        self.state.update(*action)


    def send_map(self):
        return self.state.map_array

    def goal_test(self):
        if any(1 in sublist for sublist in self.state.map_array):
            return False
        return True
