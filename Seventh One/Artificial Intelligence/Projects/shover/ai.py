class Agent:
    def __init__(self, env_percieve):
        self.percieve = env_percieve

    def heuristic(self, state):
        ######### EDITABLE SECTION #########
        pass
        ######### END OF EDITABLE SECTION #########

    def act(self):

        ######### EDITABLE SECTION #########

        import random
        mapp=self.percieve()
        w, h = len(mapp[0])-1, len(mapp)-2
        validAction = False
        while not validAction:
            direction = random.choice(["right", "left", "up", "down"])
            agentY, agentX = mapp[-1]
            tileCheck = False
            if direction == 'right' and mapp[agentY][agentX+1] not in [-2,-1]:
                i, j = agentY, agentX+1
                tileCheck = True
            elif direction == 'left' and mapp[agentY][agentX-1] not in [-2,-1]:
                i, j = agentY, agentX-1
                tileCheck = True
            elif direction == 'up' and mapp[agentY-1][agentX] not in [-2,-1]:
                i, j = agentY-1, agentX
                tileCheck = True
            elif direction == 'down' and mapp[agentY+1][agentX] not in [-2,-1]:
                i, j = agentY+1, agentX
                tileCheck = True
            if tileCheck:
                if i in range(1, h) and j in range(1, w):
                    validAction = True

        ######### END OF EDITABLE SECTION #########

        # Packs action as (i, j, direction)
        action = i, j, direction
        return action


class InternalState:
    def __init__(self):
        pass
    # nothing here, move on
