# https://school.programmers.co.kr/learn/courses/30/lessons/152995
def solution(scores):
    answer = 1

    wanho, wanho_sum = scores[0], sum(scores[0])
    max_r = 0
    for score in sorted(scores[1:], key=lambda x: (-x[0], x[1])):
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1

        if score[1] < max_r:
            continue

        if sum(score) > wanho_sum:
            answer += 1
        max_r = score[1]

    return answer


print(solution([[1, 4], [2, 4], [3, 4], [1, 4]]), 3)
print(solution([[5, 4], [2, 2]]), 1)
print(solution([[5, 4], [6, 5]]), -1)
print(solution([[1, 4]]), 1)
print(solution([[1, 4], [1, 4]]), 1)
print(solution([[2, 2], [4, 4], [3, 2], [3, 2], [2, 1]]), -1)
print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]), 4)
print(solution([[2, 2], [1, 4], [3, 3], [3, 2], [2, 1]]), -1)
print(solution([[1, 4], [1, 4], [3, 2], [3, 2]]), 1)
print(solution([[1, 4], [4, 4], [3, 3], [3, 3], [3, 3]]), 2)
print(solution([[2, 2], [1, 4], [3, 2], [3, 2]]), 4)
print(solution([[5, 4], [6, 4]]), 2)
print(solution([[1, 4], [4, 4], [4, 3], [3, 3], [3, 3]]), 3)
print(solution([[i, 100000] for i in range(100000, -1, -1)]), 1)
