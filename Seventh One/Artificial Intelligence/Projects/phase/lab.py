from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    def __init__(self,vertices): 
  
        # No. of vertices 
        self.V = vertices 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function to perform a Depth-Limited search 
    # from given source 'src' 
    def DLS(self,src,target,maxDepth): 
  
        if src == target : return True
  
        # If reached the maximum depth, stop recursing. 
        if maxDepth <= 0 : return False
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    return True
        return False
  
    # IDS to search if target is reachable from v. 
    # It uses recursive DLS() 
    def IDS(self,src, target, maxDepth): 
  
        # Repeatedly depth-limit search till the 
        # maximum depth 
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False
  
# Create a graph given in the above diagram 
g = Graph (7); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
  
target = 6; maxDepth = 3; src = 0
  
if g.IDS(src, target, maxDepth) == True: 
    print ("Target is reachable from source " +
        "within max depth") 
else : 
    print ("Target is NOT reachable from source " +
        "within max depth") 

quit()

def UCS_agent(self):
        from env import Env
        from copy import deepcopy

        queue = []
        visited = []

        # append enviorment and
        queue.append((Env(self.perceive()), []))
        while queue:
            # find state with least cost
            min_cost = float('inf')
            target_i = None
            for i, (s, action_path) in enumerate(queue):
                if min_cost > s.send_cost():
                    min_cost = s.send_cost()
                    target_i = i

            s, action_path = queue.pop(target_i)
            visited.append(s)

            # check for win
            if s.goal_test(): return action_path

            # generate an action and expand
            for i in range(1, len(s.send_map()) - 1):
                for j in range(1, len(s.send_map()[0]) - 1):
                    if s.send_map()[i][j] == 1:
                        for direction in ["down", "up", "right", "left"]:
                            new_action = Action(i, j, direction)

                            new_state = deepcopy(s)
                            new_state.take_action(new_action.return_action())

                            # check if s is visited
                            state_is_visited = False
                            for v in visited:
                                if v == new_state: state_is_visited = True

                            if not state_is_visited: queue.append((new_state, action_path + [new_action]))