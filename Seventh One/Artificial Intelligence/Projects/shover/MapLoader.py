class ChallengeDesigner:
    def run(self, command, height=False, width=False):
        if command == "load":
            return self.load_map()

        elif command == "create" and type(height) is int and type(width) is int:
            return self.create_map(height, width)
        else: raise ValueError("wrong arg sent to map creator")

    def create_map(self, height, width):

        ######### EDITABLE SECTION #########
        # Here goes how a map is generated, entered by an input or received from reading a text file
        import random
        map_array = [[random.choices([-2, 0,1], weights=[30, 30,10])[0] for j in range(width)] for i in range(height)]
        for i in [0,height-1]:
            for j in range(len(map_array[i])):
                map_array[i][j] = random.choices([-2,-1], weights=[20,90])[0]
        for i in range(len(map_array)):
            for j in [0,width-1]:
                map_array[i][j] = random.choices([-2,-1], weights=[20,90])[0]
        
        
        for i in range(1, len(map_array)-1):
            for j in range(1, len(map_array[0])-1):
                neighbours = [
                    map_array[i][j+1],
                    map_array[i][j-1],
                    map_array[i+1][j],
                    map_array[i-1][j],
                    map_array[i+1][j-1],
                    map_array[i-1][j-1],
                    map_array[i+1][j+1],
                    map_array[i-1][j+1],
                ]

                # removing impossible paths
                if map_array[i][j] == -2 and neighbours.count(-2)+neighbours.count(-1) >= 2: 
                    # map_array[i][j] = -2
                    idx = random.choice([i for i in range(len(neighbours))])
                    # neighbours[idx] = 0
                    map_array[i][j] = 0

                # unmovable boxes
                if map_array[i][j] == 1 and neighbours[:4].count(-2) >= 2: 
                    # map_array[i][j] = -2
                    idx = random.choice([i for i in range(len(neighbours))])
                    # neighbours[idx] = 0
                    map_array[i][j] = 0



        # find a place for agent in the map
        agentX = random.randint(1, width-2)
        agentY = random.randint(1, height-2)
        map_array[agentY][agentX] = 2
        map_array.append((agentY, agentX))
        ######### END OF EDITABLE SECTION ##########

        return (map_array)

    def load_map(self):
        import pickle

        map_array = pickle.load(open("map.pickle", "rb"))
        return map_array

    def save_map(self, map_array):
        import pickle
        pickle.dump(map_array, open("map.pickle","wb"))