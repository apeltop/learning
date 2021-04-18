# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    h_index = 0
    for i in range(n):
        if citations[i] > i:
            h_index += 1
    return h_index


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([3, 0, 6, 1, 5, 0, 0, 0, 0]))  # 3
print(solution([10, 8, 5, 4, 3]))  # 4
print(solution([10, 8, 5, 3, 3]))  # 3
