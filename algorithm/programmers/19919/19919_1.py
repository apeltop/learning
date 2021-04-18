import math


def solution(num):
    answer = str(num)
    halfIndex = int(len(answer) / 2)

    if int(len(answer)) % 2 == 1:
        answer += "0"

    while math.prod([int(answer[i]) for i in range(0, halfIndex)]) != math.prod([int(answer[i]) for i in range(halfIndex, len(answer))]):
        answer = str(int(answer) + 1)
        if int(len(answer)) % 2 == 1:
            answer += "0"

    return int(answer)


print(solution(1))  # 11
print(solution(111))  # 1111
print(solution(21))  # 22
print(solution(3462))  # 3462
print(solution(235386))  # 235516
