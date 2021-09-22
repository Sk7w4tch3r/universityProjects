from param import *
from copy import deepcopy
from collections import deque
from GUI import *
from utils import *
import sys
from board import *
from utils import bfs
import numpy as np




class HeuristicMaker:
    

    def __init__(self, board, playerNumber):
        self.c1 =   0.6
        self.c2 =   0.6001
        self.c3 =   14.45
        self.c4 =   6.52
        self.board  =   board
        
        if playerNumber == 1:
            self.player =   board.get_player1()
            self.rivalPlayer    =   board.get_player2()

        elif playerNumber == 2:
            self.player =   board.get_player2()
            self.rivalPlayer    =   board.get_player1()

    def get_constances(self):
        return [self.c1, self.c2, self.c3, self.c4]

    def f1(self, player):
        # in case of AI
        if self.player.get_player_number() == 1:
            return self.player.get_player_x()//2
        elif self.player.get_player_number() == 2:
            return 8 - self.player.get_player_x()//2

    def f2(self):

        if self.player.get_player_number() == 1:
            return self.f1(self.player) - self.f1(self.board.get_player2())
        elif self.player.get_player_number() == 2:
            return self.f1(self.player) - self.f1(self.board.get_player1())


    def f3(self):
        return len(bfs(self.player, self.board, self.player.get_player_x()+2))
        # return len(bfs(self.player, self.board))
    
    
    def f4(self):
        return len(bfs(self.rivalPlayer, self.board, self.player.get_player_x()-2))
        # return len(bfs(self.rivalPlayer, self.board))


    def get_heuristic_value(self):
        weights = self.get_constances() 
        heuristic_value = weights[0]*self.f1(self.player)\
        + weights[1]*self.f2() + weights[2]*self.f3()\
        + weights[3]*self.f4() + np.random.uniform()
        # print('____________________')
        # print(self.f1(self.player))
        # print(self.f2())
        # print(self.f3())
        # print(self.f4())
        # print('____________________')

        # print(heuristic_value)
        return heuristic_value


def heuristic(state, playerNumber):

    heuristicMaker = HeuristicMaker(state, playerNumber)
    
    return heuristicMaker.get_heuristic_value()

def makeChild(state,playerNumber):
    childs  =   []
    
    player_actions  =   get_valid_moves(deepcopy(state.stateBoard), state.player1)
    wall_actions    =   get_valid_wall_moves(deepcopy(state.stateBoard), state.player1, state.player2, playerNumber)
    player_actions.extend(wall_actions)
    # print(len(player_actions))
    for action in player_actions:
        # stateBoard  =   deepcopy(state.stateBoard)
        passing_state   =   GameState(state.get_player1(), state.get_player2(), deepcopy(state.stateBoard))
        # passing_state   =   state
        newState    =   make_result(passing_state, action, state.player1, playerNumber)
        newState.actionToGetHere = action
        print(newState.actionToGetHere)
        childs.append(newState)
    # print(len(childs))
    return childs



def minimaxAlphaBeta(state, depth, alpha, beta, maxPlayer):
    
    if depth==0:
        print('zero ', depth)
        return heuristic(state, maxPlayer)
    
    if maxPlayer == 1:
        print('maxplayer depth', depth)
        maxEval = -sys.maxsize-1
        action_childs = makeChild(state, 1)
        # actions = [i[1] for i in action_childs]
        # childs = [i[0] for i in action_childs]
        print(len(action_childs))
        count = 0
        for child in action_childs:
            count += 1
            eval = minimaxAlphaBeta(child, depth-1, alpha, beta, 2)
            maxEval = max(maxEval,eval)
            if maxEval == eval:
                res = eval
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        return res

    else:
        print('minplayer depth', depth)
        minEval = sys.maxsize
        action_childs = makeChild(state, 2)
        print(len(action_childs))

        for child in action_childs:
            eval = minimaxAlphaBeta(child, depth-1, alpha , beta, 1)
            print(eval)
            minEval = min(minEval,eval)
            if minEval == eval:
                res = eval
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return res


def best_next_move(state, player):
    # exploredSetPlayer1.clear()
    # exploredSetPlayer2.clear()
    value = minimaxAlphaBeta(state, miniMaxDepth, initialAlpha, initialBeta, player.get_player_number())
    # print('*****')
    # print(player.get_player_x()//2)
    # print(player.get_player_y()//2)
    # print('*****')

    return state.actionToGetHere


