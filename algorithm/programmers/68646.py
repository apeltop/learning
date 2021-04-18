# https://programmers.co.kr/learn/courses/30/lessons/68646
def solution(a):
    if len(a) == 1:
        return 1

    answer = 2

    bDict = {}
    for i, b in enumerate(sorted(a, reverse=True)):
        bDict[b] = i

    lMin = a[0]
    del bDict[lMin]

    rMin = bDict.popitem()[0]

    for i in range(1, len(a) - 1):
        if a[i] < lMin or a[i] <= rMin:
            answer += 1

            if a[i] < lMin:
                lMin = a[i]
            if a[i] == rMin:
                rMin = bDict.popitem()[0]
                continue
        del bDict[a[i]]

    return answer


print(solution([-92, -16, 27, 65, -2, 58, -71, -68, -61, -33]))  # 5      -92, -71, -68, -61, -33
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))  # 6      -16, -92, -71, -68, -61, -33
print(solution([1, 2, 3, 4, 5]))  # 5
print(solution([9, -1, -5]))  # 3
print(solution([9]))  # 1
print(solution([9, 1]))  # 2
