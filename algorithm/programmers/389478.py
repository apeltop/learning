# https://school.programmers.co.kr/learn/courses/30/lessons/389478
from collections import defaultdict


def solution(n, w, num):
    answer = 0

    num_yx = (0, 0)

    maps = defaultdict(int)
    is_right = True
    y, x = 0, 0
    for i in range(1, n + 1):
        if i == num:
            num_yx = (y, x)

        maps[f'{y}_{x}'] = i
        x += 1 if is_right else -1

        if x == -1 or x == w:
            x = max(min(x, w - 1), 0)
            is_right = not is_right
            y += 1

    cur_yx = num_yx
    while maps[f'{cur_yx[0]}_{cur_yx[1]}']:
        cur_yx = (cur_yx[0] + 1, cur_yx[1])
        answer += 1

    return answer


print(solution(22, 6, 8), 3)
print(solution(13, 3, 6), 4)
