


    # def IDS(self):
    #     i = 0
    #     while dfs_limit(limit)

    def dfs_limit(self, limit):
        from env import Env
        from copy import deepcopy
        queue = []
        visited = []
        # append enviorment and
        queue.append((Env(self.perceive()), []))
        while queue:
            # find state with least cost
            # min_cost = float('inf')
            # target_i = None
            # for i, (s, action_path) in enumerate(queue):
            #     h = self.heuristic(s)
            #     if min_cost > s.send_cost()+h:
            #         min_cost = s.send_cost()+h
            #         target_i = i
            if limit == l: return None
            s, action_path = queue.pop()
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
                            for k, v in enumerate(visited):
                                if v == new_state:
                                    if v.send_cost() > new_state.send_cost():
                                        visited.pop(k)
                                        visited.append(new_state)
                                    state_is_visited = True
                                    break

                            for k, (v,_) in enumerate(queue):
                                if v == new_state:
                                    if v.send_cost() > new_state.send_cost():
                                        queue.pop(k)
                                        queue.append((new_state, action_path + [new_action]))
                                    state_is_visited = True
                                    break

                            if not state_is_visited: queue.append((new_state, action_path + [new_action]))

    def RBFS_agent(self):
        map_array = self.perceive()
        action_sequence = []
        ######### EDITABLE SECTION #########



        ######### END OF EDITABLE SECTION #########
        return action_sequence






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

    def random_agent(self):
        import random

        map_array = self.perceive()
        for i in map_array:
            print(i)
        quit()
        w, h = len(map_array[0]), len(map_array)
        for _ in range(100):
            (i, j) = (random.randint(1, h - 2), random.randint(1, w - 2))
            if map_array[i][j] == 1: break
        h_edge_dist = min(i, h - 1 - i)
        v_edge_dist = min(j, w - 1 - j)
        if h_edge_dist < v_edge_dist:
            if 2 * i < h:
                dir = 'up'
            else:
                dir = 'down'
        else:
            if 2 * j < w:
                dir = 'left'
            else:
                dir = 'right'

        return Action(i, j, dir)
