# https://school.programmers.co.kr/learn/courses/30/lessons/258705

def solution(n, tops):
    a = [0 for _ in range(len(tops))]
    b = [0 for _ in range(len(tops))]

    if tops[0] == 1:
        a[0] = 1
        b[0] = 3
    else:
        a[0] = 1
        b[0] = 2

    for x in range(1, n):
        a[x] = (a[x - 1] + b[x - 1]) % 10007
        if tops[x] == 1:
            b[x] = 2 * a[x - 1] + 3 * b[x - 1]
        else:
            b[x] = 1 * a[x - 1] + 2 * b[x - 1]
        b[x] = b[x] % 10007

    return (a[-1] + b[-1]) % 10007


print(solution(16, [i % 2 for i in range(16)]), 7225)
print(solution(15, [i % 2 for i in range(15)]), 133)
print(solution(10, [i % 2 for i in range(10)]), 5661)
print(solution(2, [0, 0]), 8)
print(solution(2, [1, 1]), 15)
print(solution(2, [0, 1]), 11)
print(solution(4, [1, 1, 0, 1]), 149)
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 7704)
