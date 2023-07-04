import copy
from collections import deque


def interval_xy_by_direction(direction, restore=False):
    x_interval, y_interval = 0, 0

    if direction == 'U':
        y_interval = -1
    elif direction == 'D':
        y_interval = 1
    elif direction == 'R':
        x_interval = 1
    elif direction == 'L':
        x_interval = -1
    return x_interval if not restore else -x_interval, y_interval if not restore else -y_interval


def calc_xy(board, cordi, direction):
    x, y = cordi
    x_interval, y_interval = 0, 0

    next_x, next_y = cordi
    while True:
        x_interval, y_interval = interval_xy_by_direction(direction)
        next_x, next_y = next_x + x_interval, next_y + y_interval

        if next_y < 0 or next_y >= len(board):
            x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
            next_x, next_y = next_x + x_interval, next_y + y_interval
            return next_x, next_y

        if next_x < 0 or next_x >= len(board[0]):
            x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
            next_x, next_y = next_x + x_interval, next_y + y_interval
            return next_x, next_y

        if board[next_y][next_x] == 'D':
            x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
            next_x, next_y = next_x + x_interval, next_y + y_interval
            return next_x, next_y

    return next_x, next_y


# '0_6_D'
# '1_6_U'
# '0_6_L'
# '0_4_D'
# '1_4_R'
# '1_6_L'
# '1_2_U'
# '0_2_D'
# '3_2_U'
# '0_2_L'
# '0_0_D'
# '2_0_R'
# '2_3_U'

# '0_6_D'
# '1_6_U'
# '0_6_L'
# '0_4_D'
# '1_4_R'
# '1_6_L'
# '1_0_D'
# '2_0_R'
# '2_3_U'

def solution(board):
    answer = 0
    min_path = []

    def move_R(cur_board, cur_x, cur_y, direction, stack, history):
        nonlocal min_path

        q = deque()

        # Mark the starting cell as visited
        # and push it into the queue
        q.append(((cur_y, cur_x), []))
        # history[f'{cur_y}_{cur_x}_{direction}'] = True

        r_y, r_x = cur_y, cur_x
        while len(q) > 0:
            cell = q.popleft()
            cur_y, cur_x = cell[0]
            paths = cell[1]
            paths.append((cur_y, cur_x))

            if min_path and len(paths) >= len(min_path):
                continue

            if f'{cur_y}_{cur_x}_{direction}' in history:
                continue

            cur_board[r_y][r_x] = '.'
            r_y, r_x = cur_y, cur_x
            cur_board[cur_y][cur_x] = 'R'

            if board[cur_y][cur_x] == 'G':
                min_path = copy.deepcopy(paths)
                # print(len(min_path), min_path)
                continue

            for i in range(4):
                seq = ['D', 'L', 'R', 'U']
                next_x, next_y = calc_xy(cur_board, (cur_x, cur_y), seq[i])
                if next_x == cur_x and next_y == cur_y:
                    continue
                q.append(((next_y, next_x), paths[::]))
                history[f'{cur_y}_{cur_x}_{direction}'] = True

    r_x, r_y = 0, 0
    for i in range(len(board)):
        board[i] = list(board[i])
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                r_x, r_y = j, i
            if board[i][j] == 'G':
                if (not i == 0 and not i >= len(board)) - 1 and (not j == 0 and not j >= len(board[0])) - 1:
                    if \
                            board[i + 1][j] == '.' and \
                                    board[i][j + 1] == '.' and \
                                    board[i + 1][j + 1] == '.' and \
                                    board[i - 1][j] == '.' and \
                                    board[i][j - 1] == '.' and \
                                    board[i - 1][j - 1] == '.' and \
                                    board[i + 1][j - 1] == '.' and \
                                    board[i - 1][j + 1] == '.':
                        return -1
    move_R(copy.deepcopy(board), r_x, r_y, 'U', [], {})

    return len(min_path) - 1 if min_path else -1

print(solution(
    ["...D..R",
     ".D.....",
     "....D.G",
     "D....DD",
     "..D...."]
))  # 1

print(solution(
    ["...D..R",
     ".D.....",
     "....D.G",
     "D....D.",
     "..D...."]
))  # -1

print(solution(
    ["...D..R",
     ".D.G...",
     "....D.D",
     "D....D.",
     "..D...."]
))  # 7

print(solution(
    ["...D..R.....................................................................................",
     ".D.G....................................................D...................................",
     "....D.D.....................D.........D.....................................................",
     "D....D...................D........................D......................D..................",
     "..DD.................D......................D...............................................",
     "..D.........D..............D..........................D.................D...................",
     "..D.....................D........................D................D.........................",
     "..D.................D..................................................D....................",
     "..D...........D............D.......................D.....................D..................",
     "..D............................D..........................D..........................D......",
     "..D.................D............................D..................D.......................",
     "..D.................................D...D..............D....................................",
     "..D........D....D...D............................D..............D...........................",
     "..D..........................D................................D.............................",
     "..D.....................................D..........................D........................",
     "..D...D......................D................D....................D........................",
     "..D................D.........................................D.........D....................",
     "..D...........D....................................................D........................",
     "..D.....................D.............D........................D............................",
     "..D...............................................................D.........................",
     "..D..................D..................D......................D............................",
     "..D............................D............................................................",
     "..D..................................D.........................D...........................D",
     ]
))  # 7

print(solution([
    ".D.R",
    "....",
    ".G..",
    "...D"
]))  # -1

# v1
# import copy
#
#
# def interval_xy_by_direction(direction, restore=False):
#     x_interval, y_interval = 0, 0
#
#     if direction == 'U':
#         y_interval = -1
#     elif direction == 'D':
#         y_interval = 1
#     elif direction == 'R':
#         x_interval = 1
#     elif direction == 'L':
#         x_interval = -1
#     return x_interval if not restore else -x_interval, y_interval if not restore else -y_interval
#
#
# def calc_xy(board, cordi, direction):
#     x, y = cordi
#     x_interval, y_interval = 0, 0
#
#     next_x, next_y = cordi
#     while True:
#         x_interval, y_interval = interval_xy_by_direction(direction)
#         next_x, next_y = next_x + x_interval, next_y + y_interval
#
#         if next_y < 0 or next_y >= len(board):
#             x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
#             next_x, next_y = next_x + x_interval, next_y + y_interval
#             return next_x, next_y
#
#         if next_x < 0 or next_x >= len(board[0]):
#             x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
#             next_x, next_y = next_x + x_interval, next_y + y_interval
#             return next_x, next_y
#
#         if board[next_y][next_x] == 'D':
#             x_interval, y_interval = interval_xy_by_direction(direction, restore=True)
#             next_x, next_y = next_x + x_interval, next_y + y_interval
#             return next_x, next_y
#
#     return next_x, next_y
#
#
# def solution(board):
#     answer = 0
#     min_path = []
#
#     def move_R(cur_board, cur_x, cur_y, direction, stack, history):
#         nonlocal min_path
#
#         if min_path and len(stack) >= len(min_path) - 1:
#             if stack:
#                 stack.pop()
#             return
#
#         if f'{cur_y}_{cur_x}_{direction}' in history:
#             if stack:
#                 stack.pop()
#             return
#
#         next_x, next_y = calc_xy(cur_board, (cur_x, cur_y), direction)
#         if next_x == cur_x and next_y == cur_y:
#             if stack:
#                 stack.pop()
#             return
#
#         stack.append(f'{cur_y}_{cur_x}_{direction}')
#         history[f'{cur_y}_{cur_x}_{direction}'] = True
#         cur_board[cur_y][cur_x] = '.'
#         cur_board[next_y][next_x] = 'R'
#         if board[next_y][next_x] == 'G':
#             min_path = copy.deepcopy(stack)
#             return
#
#         move_R(cur_board[::], next_x, next_y, 'U', stack[::], history.copy())
#         move_R(cur_board[::], next_x, next_y, 'D', stack[::], history.copy())
#         move_R(cur_board[::], next_x, next_y, 'R', stack[::], history.copy())
#         move_R(cur_board[::], next_x, next_y, 'L', stack[::], history.copy())
#
#     r_x, r_y = 0, 0
#     for i in range(len(board)):
#         board[i] = list(board[i])
#         for j in range(len(board[i])):
#             if board[i][j] == 'R':
#                 r_x, r_y = j, i
#     move_R(copy.deepcopy(board), r_x, r_y, 'U', [], {})
#     move_R(copy.deepcopy(board), r_x, r_y, 'D', [], {})
#     move_R(copy.deepcopy(board), r_x, r_y, 'R', [], {})
#     move_R(copy.deepcopy(board), r_x, r_y, 'L', [], {})
#
#     return len(min_path) if min_path else -1
#
#
# print(solution(
#     ["...D..R",
#      ".D.G...",
#      "....D.D",
#      "D....D.",
#      "..D...."]
# ))  # 7
#
# print(solution([
#     ".D.R",
#     "....",
#     ".G..",
#     "...D"
# ]))  # -1
