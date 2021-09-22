from param import *
from copy import deepcopy
from utils import make_result
# from Game import Player
# import Game.GameState
from collections import deque
from GUI import *
from utils import *



class HeuristicMaker:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def get_constances(self):
        return [self.c1, self.c2, self.c3, self.c4]


def heuristic(state, heuristicMaker):
    #guide :))))
    path1 = len(bfs(state.get_player1(), state))
    path2 = len(bfs(state.get_player2(), state))
    
    return evaluation



def minimaxAlphaBeta(state, depth, alpha, beta, maxPlayer, heuristicMaker):
    pass

def best_next_move(state, player, heuristicMaker):
    exploredSetPlayer1.clear()
    exploredSetPlayer2.clear()
    minimaxAlphaBeta(state, miniMaxDepth, initialAlpha, initialBeta, player, heuristicMaker)
    return state.nextMove


