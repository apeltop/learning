# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = sum([v for v in range(min(a, b), max(a, b) + 1)])
    return answer


print(solution(3, 5))  # 12
print(solution(3, 3))  # 3
print(solution(5, 3))  # 12
