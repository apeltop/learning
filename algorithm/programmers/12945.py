# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    i = 0
    cur, nxt = 0, 1

    while i < n:
        cur, nxt = nxt, cur + nxt
        i += 1

    return cur % 1234567


print(solution(0))  # 0
print(solution(1))  # 1
print(solution(3))  # 2
print(solution(5))  # 5
