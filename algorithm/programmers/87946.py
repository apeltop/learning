from itertools import permutations


def solution(k, dungeons):
    answer = -1

    cases = list(permutations([i for i in range(len(dungeons))]))
    for case in cases:
        remain_k, count = k, 0
        for i in list(case):
            if remain_k < dungeons[i][0]:
                break

            remain_k -= dungeons[i][1]
            count += 1

        if answer < count:
            answer = count
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
print(solution(80, [[80, 20], [50, 40], [30, 10], [80, 20], [50, 40], [30, 10], [80, 20], [50, 40]]))  # 3
