def alpha_beta_search(board):
    return max_value(board, -2, 2)


def max_value(board, alpha, beta):
    terminal = is_terminal(board)
    if terminal[0]:
        return (board, 1) if terminal[1] == 1 else (board, -1) if terminal[1] == -1 else (board, 0)
    final_board = None
    v = -2
    _board = bin(sum([abs(x) for x in board]))[2:]
    _board = "0" * (9 - len(_board)) + _board
    for i in range(len(_board)):
        if _board[i] == "0":
            successor_board = board + [2 ** (8 - i)]
            min_val = min_value(successor_board, alpha, beta)
            if min_val[1] > v:
                v = min_val[1]
                final_board = successor_board
            if v >= beta:
                return successor_board, v
            alpha = max(alpha, v)
    return final_board, v


def min_value(board, alpha, beta):
    terminal = is_terminal(board)
    if terminal[0]:
        return (board, 1) if terminal[1] == 1 else (board, -1) if terminal[1] == -1 else (board, 0)
    final_board = None
    v = 2
    _board = bin(sum([abs(x) for x in board]))[2:]
    _board = "0" * (9 - len(_board)) + _board
    for i in range(len(_board)):
        if _board[i] == "0":
            successor_board = board + [-(2 ** (8 - i))]
            max_val = max_value(successor_board, alpha, beta)
            if max_val[1] < v:
                v = max_val[1]
                final_board = successor_board
            if v <= alpha:
                return successor_board, v
            beta = min(beta, v)
    return final_board, v


def is_terminal(board):
    w = [0b111, 0b111000, 0b111000000, 0b1001001, 0b10010010, 0b100100100, 0b100010001, 0b1010100]
    return (True, 1) if len(
        [x for x in [x & sum([x if x > 0 else 0 for x in board]) for x in w] if x in w]) > 0 else (True, -1) if len(
        [x for x in [x & sum([-x if x < 0 else 0 for x in board]) for x in w] if x in w]) > 0 else (True, 0) if sum(
        [abs(x) for x in board]) == 0b111111111 else (False, None)


def print_board(board):
    result = ""
    for i in range(9):
        if 2 ** i in board:
            result += "*"
        elif -(2 ** i) in board:
            result += "-"
        else:
            result += "^"
        if i in [2, 5]:
            result += "\n"
    print result, "\n"


startBoard = []
print_board(startBoard)
while True:
    startBoard = alpha_beta_search(startBoard)[0]
    print_board(startBoard)
    is_t = is_terminal(startBoard)
    if is_t[0]:
        print "You lose!" if is_t[1] == 1 else "You win!" if is_t[1] == -1 else "Finish!"
        break
    startBoard += [-(2 ** (int(input("Enter cell number(1 to 9, left to right, top to down): ")) - 1))]
    print_board(startBoard)
    is_t = is_terminal(startBoard)
    if is_t[0]:
        print "You lose!" if is_t[1] == 1 else "You win!" if is_t[1] == -1 else "Finish!"
        break
