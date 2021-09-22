import random
from GUI import *
from board import *
from collections import deque
from copy import deepcopy
from ai_player import best_next_move, HeuristicMaker
from utils import (
    is_wall_clicked, 
    set_moving_wall, 
    is_valid_wall,
    show_valid_moves,
    get_valid_moves,
    check_for_not_stulking,
    is_valid_move,
    get_valid_wall_moves, 
    win,
    bfs, 
    GameState
)

board = []



action_list = [276, 242, 208, 174, 140, 106, 72, 38, 4]
def AI_move_VS_Human(currentBoard, player1, player2):
    import numpy as np

    # player 1 is the AI
    newPlayer1 = Player(1, player1.get_square_number(), 1, currentBoard)
    newPlayer2 = Player(2, player2.get_square_number(), 1, currentBoard)
    newPlayer1.set_num_of_walls(player1.get_num_of_walls())
    newPlayer2.set_num_of_walls(player2.get_num_of_walls())
    currentState = GameState(newPlayer1, newPlayer2, currentBoard)
    action = best_next_move(currentState, newPlayer1)
    print(newPlayer2.get_player_x()//2)
    print(newPlayer2.get_player_y()//2)
    # action = action_list.pop()

    # Action is simply the new position (int)=
    print("best : ", action)
    # print(player1.get_square_number())
    
    # moving the player (0, 2, 4, ...)
    if action % 2 == 0:
        print('player', action)
        player1.set_square_number(action, board)
        player1.rect.x = board[player1.get_square_number()].get_rect().x + 8
        player1.rect.y = board[player1.get_square_number()].get_rect().y + 8    

    # place vertical wall (1, 3, 5,...)
    elif int(action / 17) % 2 == 0:
        print('simple wall', action)
        for i in walls:
            if i.get_player_number() == 1 and i.get_square_number() == -1:
                i.set_square_number(action, board)
                i.rect.x = board[i.get_square_number()].get_rect().x
                i.rect.y = board[i.get_square_number()].get_rect().y
                player1.set_num_of_walls(player1.numberOfWalls - 1)
                break

    # horizontal wall (19, 23, ...)
    elif int(action / 17) % 2 == 1:
        print('rotated wall', action)
        for i in walls:
            if i.get_player_number() == 1 and i.get_square_number() == -1:
                i.rotate_wall(0, 0, 0, 0)
                i.set_square_number(action, board)
                print(i.get_voh())
                i.rect.x = board[i.get_square_number()].get_rect().x
                i.rect.y = board[i.get_square_number()].get_rect().y
                player1.set_num_of_walls(player1.numberOfWalls - 1)
                break

mode = 0


playerNumber = 2
if playerNumber == 1:
    print("AI starts")
else:
    print("You start")

set_board(board)

pygame.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player1 = Player(1, 8, 2, board)
player2 = Player(2, 280, 2, board)

walls = []
# initialState
currentState = GameState(player1, player2, deepcopy(board))


all_sprites.add(player1)
all_sprites.add(player2)
board[8].set_contaning_beam(True)
board[280].set_contaning_beam(True)

for i in range(1, 11):
    walls.append(WallSprite(1, i, 1, 2))
    walls.append(WallSprite(1, i, 2, 2))



for wall in walls:
    all_sprites.add(wall)

window = pygame.display.set_mode((windowWidth, windowHeight))
window0 = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Quoridor by Sarah and Mesmol")

player_draging = False
wall_draging = False
show_valid_player_moves = 0
run = True
mode_ai_turn = 1

while bool(run):
    pygame.time.delay(100)
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                LEFT_CLICK = True
                # -- move player --
                if player2.rect.collidepoint(event.pos):
                    if playerNumber == 2:
                        moving_player = player2
                        show_valid_player_moves = 2
                        player_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = moving_player.rect.x - mouse_x
                        offset_y = moving_player.rect.y - mouse_y

                elif player1.rect.collidepoint(event.pos):
                    print("Don't touch the AI")

                
                        # -- move wall --
                if is_wall_clicked(walls, event):
                    moving_wall = set_moving_wall(walls, event)
                    if moving_wall.get_player_number() == playerNumber and moving_wall.get_square_number() == -1:
                        mouse_x, mouse_y = event.pos
                        offset_x = moving_wall.rect.x - mouse_x
                        offset_y = moving_wall.rect.y - mouse_y
                        wall_draging = True
                    else:
                        print("don't touch this wall!")

            if event.button == 3 and LEFT_CLICK and wall_draging:
                moving_wall.rotate_wall(mouse_x, offset_x, mouse_y, offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if player_draging:
                    for s in board:
                        if s.get_rect().collidepoint(event.pos):
                            newSquareNumber = s.get_number()
                            if (is_valid_move(moving_player, newSquareNumber, board)):
                                moving_player.set_square_number(newSquareNumber, board)
                                moving_player.rect.x = board[moving_player.get_square_number()].get_rect().x + 8
                                moving_player.rect.y = board[moving_player.get_square_number()].get_rect().y + 8
                                
                                AI_move_VS_Human(deepcopy(board), player1, player2)

                        else:
                            moving_player.rect.x = board[moving_player.get_square_number()].get_rect().x + 8
                            moving_player.rect.y = board[moving_player.get_square_number()].get_rect().y + 8
                    player_draging = False
                    show_valid_player_moves = 0
                    LEFT_CLICK = False

                if wall_draging:
                    for s in board:
                        if s.get_rect().collidepoint(event.pos):
                            newSquareNumber = s.get_number()
                            if (is_valid_wall(newSquareNumber, board, moving_wall)):
                                moving_wall.set_square_number(newSquareNumber, board)
                                placed_wall = True
                                moving_wall.rect.x = board[moving_wall.get_square_number()].get_rect().x
                                moving_wall.rect.y = board[moving_wall.get_square_number()].get_rect().y
                                if mode == 0:
                                    if check_for_not_stulking(player1, board) == False or check_for_not_stulking(
                                            player2, board) == False:
                                        if moving_wall.get_voh() != moving_wall.initial_voh():
                                            moving_wall.rotate_wall(mouse_x, offset_x, mouse_y, offset_y)
                                        moving_wall.set_square_number(-1, board)
                                        print("invalid wall placement")
                                        placed_wall = False
                                        moving_wall.rect.x, moving_wall.rect.y = moving_wall.get_coordinates()

                                
                                if placed_wall == True:
    
                                    AI_move_VS_Human(deepcopy(board), player1, player2)

                                    
                            else:
                                if (moving_wall.get_voh() != moving_wall.initial_voh()):
                                    print("not valid")
                                    moving_wall.rotate_wall(mouse_x, offset_x, mouse_y, offset_y)
                                moving_wall.set_square_number(-1, board)
                                moving_wall.rect.x, moving_wall.rect.y = moving_wall.get_coordinates()

                    wall_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if player_draging:
                mouse_x, mouse_y = event.pos
                moving_player.rect.x = mouse_x + offset_x
                moving_player.rect.y = mouse_y + offset_y
            if wall_draging:
                mouse_x, mouse_y = event.pos
                moving_wall.rect.x = mouse_x + offset_x
                moving_wall.rect.y = mouse_y + offset_y

    pygame.draw.rect(window, backGroundColor, (0, 0, windowWidth, windowHeight))
    draw_board(board, window)
    
    # if showPath == True:
    #     for i in bfs(player1, newState):
    #         pygame.draw.rect(window, (255, 255, 255), board[i].get_rect())

    if show_valid_player_moves == 1 or mode == 0:
        show_valid_moves(player1, window, board)
    if show_valid_player_moves == 2:
        show_valid_moves(player2, window, board)
    if show_valid_player_moves == 3:
        show_valid_moves(player3, window, board)
    if show_valid_player_moves == 4:
        show_valid_moves(player4, window, board)
    all_sprites.update()
    all_sprites.draw(window)


    newPlayer1 = Player(1, player1.get_square_number(), 1, deepcopy(board))
    newPlayer2 = Player(2, player2.get_square_number(), 1, deepcopy(board))
    newState = GameState(newPlayer1, newPlayer2, deepcopy(board))

    # winning
    if win(player1):
        print("Player1 won!")
        run = False
    if win(player2):
        print("Player2 won!")
        run = False

    pygame.display.update()
