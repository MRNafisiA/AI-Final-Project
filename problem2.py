import math
import random


def get_randomized_board():
    board = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(board)
    return board


def evaluate(board):
    checks = 0
    for _x in range(len(board)):
        for _y in range(_x + 1, len(board)):
            if board[_x] == board[_y] or abs(board[_y] - board[_x]) == _y - _x:
                checks += 1
    return checks


def schedule(i):
    return 1000.0 - i


bestBoard = get_randomized_board()
time = 1
while True:
    if evaluate(bestBoard) == 0:
        for x in range(len(bestBoard)):
            row = ""
            for y in range(len(bestBoard)):
                if y == bestBoard[x]:
                    row += "*"
                else:
                    row += " "
            print row
        print bestBoard
        break
    nextBoard = get_randomized_board()
    if evaluate(bestBoard) > evaluate(nextBoard) or random.random() > math.exp(
            (evaluate(bestBoard) - evaluate(nextBoard)) / schedule(time)):
        bestBoard = nextBoard
    time += 1
