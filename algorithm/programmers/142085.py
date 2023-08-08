from heapq import heappush, heappop


def solution(n, k, enemy):
    answer = 0

    heap = []
    for i, e in enumerate(enemy):
        heappush(heap, e)

        if len(heap) > k:
            n -= heappop(heap)

        if n < 0:
            return i

    return len(enemy)


print(solution(7, 3, [1, 2, 4, 5, 3, 3, 1]), 7)

print(solution(3, 4, [3, 3, 3, 3, 3]), 5)

print(solution(7, 3, [1]), 1)
print(solution(7, 3, [8, 8, 8, 8]), 3)
print(solution(7, 3, [9, 7, 1, 1, 1, 1, 1]), 7)
print(solution(7, 3, [9, 6, 1, 1, 1, 1, 1]), 7)

print(solution(8, 3, [1, 2, 4, 5, 3, 3, 1]), 7)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]), 5)
print(solution(4, 4, [3, 3, 3, 3, 3]), 5)
print(solution(2, 4, [3, 3, 3, 3, 3]), 4)
print(solution(4, 0, [3, 3, 3, 3]), 1)
print(solution(2, 4, [3, 3, 3, 3]), 4)
print(solution(1, 0, [3, 3, 3, 3]), 0)

print(solution(1000000000, 1, [3 for i in range(1000000)]), 5)
print(solution(1000000, 1, [3 for i in range(1000000)]), 5)

# import copy
# from collections import deque
#
#
# def solution(n, k, enemy):
#     answer = 0
#     enemy = deque(enemy)
#     enemy_count = len(enemy)
#
#     def bfs():
#         q = deque()
#         max_round = 0
#
#         q.append((n, k, 0))
#
#         while q:
#             # print(len(q))
#             sol, skill_count, enemies_index = q.popleft()
#
#             if len(enemy) == enemies_index:
#                 continue
#
#             if sol < 1:
#                 continue
#
#             if sol < enemy[enemies_index] and skill_count <= 0:
#                 continue
#
#             if enemies_index + 1 > max_round:
#                 max_round = enemies_index + 1
#
#             q.append((sol - enemy[enemies_index], skill_count, enemies_index + 1))
#             if skill_count > 0:
#                 q.append((sol, skill_count - 1, enemies_index + 1))
#
#         return max_round
#
#     return bfs()
