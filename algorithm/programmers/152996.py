# https://school.programmers.co.kr/learn/courses/30/lessons/152996
# https://school.programmers.co.kr/questions/48895
import collections


def solution(weights):
    answer = 0
    counter = collections.Counter(weights)

    for i in range(100, 1001):
        if counter[i] > 0:
            answer += counter[i] * (counter[i] - 1) // 2
            answer += counter[i] * counter[i * 2 / 3]
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 3 / 4]

    return answer


#
# print(solution([100, 180, 360, 100, 270, 240, 480, 180]), 8)
# print(solution([8, 6]), 1)
# print(solution([100, 180, 360, 100, 270]), 4)
# print(solution([100, 180, 360, 100, 270, 240]), 6)
print(solution([100, 100, 100, 100]), 6)
print(solution([100, 180, 360, 100, 270, 240, 480]), 8)
print(solution([119, 119, 100, 119 * 2]), 1)
print(solution([100, 150, 200]), 3)
print(solution([100, 101, 102]), 0)
print(solution([100, 300]), 0)
print(solution([111, 111, 100, 111]), 1)
print(solution([111, 111, 100, 111, 100]), 2)
print(solution([107, 428]), 0)
# print(solution([random.randint(100, 1000) for i in range(100000)]), 2)
