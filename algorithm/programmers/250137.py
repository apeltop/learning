from collections import deque


def solution(bandage, health, attacks):
    attacks = deque(sorted(attacks))

    cur_health = health
    healing_count = 0

    for i in range(1, attacks[-1][0] + 1):
        if cur_health <= 0:
            break

        attack = attacks[0]
        if attack[0] == i:
            cur_health -= attack[1]
            healing_count = 0

            attacks.popleft()
        else:
            cur_health = min(health, cur_health + bandage[1])
            healing_count += 1

            if healing_count == bandage[0]:
                cur_health = min(health, cur_health + bandage[2])
                healing_count = 0

    return cur_health if cur_health > 0 else -1


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]), 5)
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]), -1)
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]), -1)
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]), 3)
