import copy
import time
class Agent:
    def __init__(self, env_perception):
        # YOU CAN CHOOSE AGENT TYPE HERE, LOOK AT AGENT_TYPE_DICT TO FIND OUT OTHER CHOICES
        self.agent_type = "IDS"

        # A DICTIONARY OF AVAILABLE AGENT ALGORITHMS. YOU CAN ADD UP MORE TO THIS LIST IF YOU WISH.
        self.agent_type_dict = {

            "A_Star": self.A_Star_agent,
            "IDS": self.IDS_agent,
            # "RBFS": self.RBFS_agent,
            # "random": self.random_agent,

        }

        self.perceive = env_perception
        self.sequence=[]

    # Algorithms which return an *action sequence* or a *single action*

    def print_map(self, array):
        for i in array:
            print(i)
        print('______________________')

    def IDS_agent(self):
        import numpy as np
        map_array = self.perceive()
        # map_array = np.array(map_array)
        action_sequence = []
        ######### EDITABLE SECTION #########

        root    = Node(copy.deepcopy(map_array), None)
        # start_time = time.process_time()
        root.create_children()
        # print(len(root.child))
        # print(f'created childs for root in {time.process_time()-start_time} msecs.')

        limit   = 1
        res     = root
        while not (res.goal==True):
            visited = []
            res = self.DLS(root, visited, limit)
            print(len(visited))
            # if type(res) == bool:

            self.print_map(res.map)
            limit += 1
        
        action_sequence = res.get_actions()

        
        ######### END OF EDITABLE SECTION #########
        return action_sequence
    
    def DLS(self, root, visited, limit):
        visited.append(root)

        if root.goal == True:
            # print('returning root with goal == bool (True)')
            print(root.goal)
            return root
        if limit<=0:
            # print('depth limit exceeded')
            # root.goal = False
            return root
        # print(len(root.child))
        for node in root.child:
            if node not in visited:
                # start_time = time.process_time()
                node.create_children()
                # print(f'created childs for children in {time.process_time()-start_time} msecs.')
                res = self.DLS(node, visited, limit-1)
                if res.goal:
                    # print('returning node with goal == True')
                    return res
        return root

    
    def A_Star_agent(self):
        map_array = self.perceive()
        action_sequence = []
        ######### EDITABLE SECTION #########

        root    = Node(copy.deepcopy(map_array), None)
        root.cost = 0
        # root.create_children()
        explored_set = []
        frontier = [[root, root.f]]
        # root.cost = root.score
        while True:
            if not frontier: break
            node = frontier.pop(0)
            node = node[0]
            
            explored_set.append(node)
            node.create_children()
            action_set = node.child
            for action in action_set:
                if action not in frontier and action not in explored_set:
                    frontier.append([action, action.f])
                    # print(action.score)
                    frontier = sorted(frontier, key=lambda x:x[1])
                else:
                    frontier_maps = [children[0].map for children in frontier]
                    if action.map in frontier_maps:
                        sim_map = frontier_maps.index(action.map)  # index of the node with similar map
                        if action.f < frontier[sim_map][1]:
                            frontier[sim_map] = [action, action.f]
            if node.goal:
                break   # the while
            # estimates   = [[node, node.f] for node in root.child]
            # min_node    = sorted(estimates, key=lambda x: x[1])[0][0]
            # print('not goal')
            # root = min_node
            # root.create_children()



        action_sequence = node.get_actions()

        ######### END OF EDITABLE SECTION #########
        return action_sequence
    


    def act(self):
        # If sequence not empty, pops another action
        if len(self.sequence)!=0: return self.sequence.pop(0)

        # Result is whether a sequence or a single action object
        result = self.agent_type_dict[self.agent_type]()

        # check if the result was a sequence
        if isinstance(result, list) and not(False in [isinstance(ar, Action) for ar in result]):
            self.sequence = result
            return self.sequence.pop(0)

        # As it was not a sequence, this line assures the result was a valid single action
        if not isinstance(result, Action):
            raise TypeError("Agent did not return an instance of the class Action")

        return result

class Node:
    def __init__(self, map_array, parent, action=None, cost=0):
        import numpy as np
        self.map    = np.array(map_array)
        self.parent = parent
        self.action = action
        self.child  = []
        self.score  = self.heuristic(self.map)
        self.goal   = self.state()
        self.cost   = cost
        self.f      = self.cost+self.score
        self.init_cost  = 4
    def state(self):
        no_box = self.map[1:len(self.map)-1, 1:len(self.map)-1].flatten().tolist().count(1)
        if no_box == 0:
            return True
        else:
            # return no_box
            return False

    def create_children(self):   # O((n^2)/2)
        h, w = (len(self.map), len(self.map[0]))
        for i in range(h):
            for j in range(w):
                if self.map[i][j] == 1: # in case of box
                    if self.map[i][j+1] in [0, -1]:
                        child_map = copy.deepcopy(self.map)
                        child_map[i][j] = 0
                        if child_map[i][j+1] == 0:
                            child_map[i][j+1] = 1
                        self.child.append(Node(child_map, parent=self, action=Action(i, j, 'right'), cost=self.init_cost+self.cost))
                    if self.map[i][j+1] == 1:
                        child_map = copy.deepcopy(self.map)
                        child_map, flag, depth = self.adj_push(child_map, i, j, 'right')
                        if flag:
                            child_map[i][j] = 0
                            self.child.append(Node(child_map, parent=self, action=Action(i, j, 'right'), cost=self.cost+depth+self.init_cost))
                    
                    if self.map[i][j-1] in [0, -1]:
                        child_map = copy.deepcopy(self.map)
                        child_map[i][j] = 0
                        if child_map[i][j-1] == 0:
                            child_map[i][j-1] = 1
                        self.child.append(Node(child_map, parent=self, action=Action(i, j, 'left'), cost=self.init_cost+self.cost))
                    if self.map[i][j-1] == 1:
                        child_map = copy.deepcopy(self.map)
                        child_map, flag, depth = self.adj_push(child_map, i, j, 'left')
                        if flag:
                            child_map[i][j] = 0
                            self.child.append(Node(child_map, parent=self, action=Action(i, j, 'left'), cost=self.cost+depth+self.init_cost))
                    
                    if self.map[i-1][j] in [0, -1]:
                        child_map = copy.deepcopy(self.map)
                        child_map[i][j] = 0
                        if child_map[i-1][j] == 0:
                            child_map[i-1][j] = 1
                        self.child.append(Node(child_map, parent=self, action=Action(i, j, 'up'), cost=self.init_cost+self.cost))
                    if self.map[i-1][j] == 1:
                        child_map = copy.deepcopy(self.map)
                        child_map, flag, depth = self.adj_push(child_map, i, j, 'up')
                        if flag:
                            child_map[i][j] = 0
                            self.child.append(Node(child_map, parent=self, action=Action(i, j, 'up'), cost=self.cost+depth+self.init_cost))
                    
                    if self.map[i+1][j] in [0, -1]:
                        child_map = copy.deepcopy(self.map)
                        child_map[i][j] = 0
                        if child_map[i+1][j] == 0:
                            child_map[i+1][j] = 1
                        self.child.append(Node(child_map, parent=self, action=Action(i, j, 'down'), cost=self.init_cost+self.cost))
                    if self.map[i+1][j] == 1:
                        child_map = copy.deepcopy(self.map)
                        child_map, flag, depth = self.adj_push(child_map, i, j, 'down')
                        if flag:
                            child_map[i][j] = 0
                            self.child.append(Node(child_map, parent=self, action=Action(i, j, 'down'), cost=self.cost+depth+self.init_cost))
                    
    
    def adj_push(self, tmp_map, i, j, dir, depth=0):
        # tmp_map = copy.deepcopy(tmp_map)
        if tmp_map[i][j] in [0, -1]:
            if tmp_map[i][j] == 0:
                tmp_map[i][j] = 1
            # print(depth+self.init_cost)
            return (tmp_map, True, depth)
        elif tmp_map[i][j] == -2: # no further action needed
            return (tmp_map, False, 0)
        depth += 1
        if dir=='right':
            return self.adj_push(tmp_map, i, j+1, dir, depth)
        elif dir=='left':
            return self.adj_push(tmp_map, i, j-1, dir, depth)
        elif dir=='up':
            return self.adj_push(tmp_map, i-1, j, dir, depth)
        elif dir=='down':
            return self.adj_push(tmp_map, i+1, j, dir, depth)


    def heuristic(self, map) -> float:
        import numpy as np

        squares = []
        h = len(map)//2
        for i in range(1, len(map)//2):
            tmp_sq = map[h-i:h+i, h-i:h+i].flatten()
            squares.append([tmp_sq.tolist().count(1), len(tmp_sq)])
        res = [squares[0][0]/squares[0][1]]
        for i in range(1, len(squares)):
            box_num = abs(squares[i][0]-squares[i-1][0])
            all_places = abs(squares[i][1]-squares[i-1][1])
            res.append(box_num/all_places)
        mult = np.linspace(4, 1, len(res))
        res = sum(res*mult)
        return res
        # box = map.flatten().tolist().count(1)
        # places = len(map.flatten())
        # return (box/places)*2
        
    def get_actions(self):
        parents = [self]
        node    = self.parent
        while node.parent != None:
            parents.append(node)
            node = node.parent
        actions = [node.action for node in parents]
        actions.reverse()
        return actions
class Action:
    def __init__(self,i,j,direction):
        self.update(i,j,direction)

    def update(self, i, j, direction):
        # Validates the action format as (int, int, string)
        if not (isinstance(i, int) and isinstance(j, int) and isinstance(direction, str)):
            raise TypeError("x, y or direction has wrong type")

        self.x = i
        self.y = j
        self.direction = direction

    def return_action(self): return (self.x, self.y, self.direction)
