mazeX = [[True, True, True, True, True, True, True, True, True, True],
         [False, True, False, True, False, False, True, False, False, False],
         [False, False, False, False, True, True, False, True, False, False],
         [False, False, False, False, False, True, True, True, True, False],
         [False, False, True, True, False, True, True, True, True, False],
         [False, True, False, True, True, False, True, False, False, True],
         [False, False, True, False, False, True, False, False, True, False],
         [False, True, True, False, False, False, True, True, False, True],
         [False, False, False, False, True, True, True, True, False, False],
         [False, True, False, True, True, True, True, False, False, False],
         [True, True, True, True, True, True, True, True, True, True]
         ]
mazeY = [[True, False, False, True, False, True, False, False, True, False, True],
         [True, False, True, True, False, True, True, False, True, True, True],
         [True, True, True, True, True, False, False, True, False, True, True],
         [True, True, True, False, True, False, False, False, False, False, True],
         [True, True, False, False, False, True, False, False, True, False, True],
         [True, False, True, False, True, False, False, True, True, False, True],
         [True, True, False, False, False, True, False, True, False, False, True],
         [True, True, False, True, True, True, False, False, True, True, True],
         [True, True, True, True, False, False, False, False, True, True, True],
         [True, False, False, True, False, False, False, False, True, False, True]
         ]
start = (0, 0)
goal = (7, 9)


def calculate_manhattan(s, g):
    return abs(s[0] - g[0]) + abs(s[1] - g[1])


def calculate_successors(node):
    calculated_successors = []
    if not mazeX[node[0][0]][node[0][1]] and not (node[4][0] == node[0][0] - 1 and node[4][1] == node[0][1]):
        calculated_successors.append(
            ((node[0][0] - 1, node[0][1]), node[1] + 1, calculate_manhattan((node[0][0] - 1, node[0][1]), goal),
             node[3] + [(node[0][0] - 1, node[0][1])], node[0]))
    if not mazeX[node[0][0] + 1][node[0][1]] and not (node[4][0] == node[0][0] + 1 and node[4][1] == node[0][1]):
        calculated_successors.append(
            ((node[0][0] + 1, node[0][1]), node[1] + 1, calculate_manhattan((node[0][0] + 1, node[0][1]), goal),
             node[3] + [(node[0][0] + 1, node[0][1])], node[0]))
    if not mazeY[node[0][0]][node[0][1]] and not (node[4][0] == node[0][0] and node[4][1] == node[0][1] - 1):
        calculated_successors.append(
            ((node[0][0], node[0][1] - 1), node[1] + 1, calculate_manhattan((node[0][0], node[0][1] - 1), goal),
             node[3] + [(node[0][0], node[0][1] - 1)], node[0]))
    if not mazeY[node[0][0]][node[0][1] + 1] and not (node[4][0] == node[0][0] and node[4][1] == node[0][1] + 1):
        calculated_successors.append(
            ((node[0][0], node[0][1] + 1), node[1] + 1, calculate_manhattan((node[0][0], node[0][1] + 1), goal),
             node[3] + [(node[0][0], node[0][1] + 1)], node[0]))
    return calculated_successors


def find_best_successor():
    max_i = 0
    for i in range(len(successors)):
        if successors[i][1] + successors[i][2] < successors[max_i][1] + successors[max_i][2]:
            max_i = i
    return max_i


successors = [(start, 0, calculate_manhattan(start, goal), [start], (-1, -1))]
while True:
    target = successors.pop(find_best_successor())
    if target[0][0] == goal[0] and target[0][1] == goal[1]:
        print target[3]
        break
    successors = successors + calculate_successors(target)
