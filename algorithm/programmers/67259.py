import copy
from collections import deque, defaultdict


def solution(board):
    answer = 0

    def is_valid_board(y, x):
        return (y >= 0 and y < len(board)) and (x >= 0 and x < len(board[0]))

    def bfs():
        commands = ['R', 'D', 'L', 'U']
        nonlocal answer
        q = deque()

        for command in commands:
            q.append(((0, 0), command, 0, {'0_0': command}))

        min_cost_dict = defaultdict(int)
        while q:
            current_position, direction, cost, history = q.popleft()
            current_y, current_x = current_position

            if not answer == 0:
                if cost > answer:
                    continue

            if current_x == len(board[0]) - 1 and current_y == len(board) - 1:
                if answer == 0:
                    answer = cost
                elif cost < answer:
                    answer = cost
                continue

            if direction == 'U':
                current_y -= 1

            if direction == 'L':
                current_x -= 1

            if direction == 'D':
                current_y += 1

            if direction == 'R':
                current_x += 1

            if not is_valid_board(current_y, current_x):
                continue

            if f'{current_y}_{current_x}' in history:
                continue

            if board[current_y][current_x] == 1:
                continue

            if history:
                cost += 100 if list(history.values())[-1] == direction else 500 + 100
            else:
                cost = 100

            history[f'{current_y}_{current_x}'] = direction

            if f'{current_y}_{current_x}' in min_cost_dict:
                if cost <= min_cost_dict[f'{current_y}_{current_x}']:
                    min_cost_dict[f'{current_y}_{current_x}'] = cost
                elif cost - 400 >= min_cost_dict[f'{current_y}_{current_x}']:
                    continue
            else:
                min_cost_dict[f'{current_y}_{current_x}'] = cost

            for command in commands:
                q.append(((current_y, current_x), command, cost, copy.copy(history)))

    bfs()
    return answer


print(solution([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]), 900)

print(solution([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)

print(solution([
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]), 7800)

print(solution([
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0]]), 2100)

print(solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]]), 3200)

print(solution([
    [0, 1, 1],
    [0, 0, 1],
    [1, 0, 0]]), 1900)

print(solution([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]]), 900)

print(solution([
    [0, 1, 1],
    [0, 1, 1],
    [0, 0, 0]]), 900)

print(solution([
    [0, 1, 1],
    [0, 0, 0],
    [0, 0, 0]]), 900)

print(solution([
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]]), 900)

print(solution([
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 0]]), 900)

print(solution([
    [0, 0, 1],
    [1, 0, 1],
    [0, 0, 0]]), 1400)

print(solution([
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]]), 1400)

print(solution([
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]]), 1400)

print(solution(
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
), 4500)
