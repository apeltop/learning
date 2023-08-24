def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B)

    while A and A[-1] >= B[-1]:
        A.pop(len(A) - 1)
        B.pop(0)

    for a in A:
        b_1 = len(B)

        for i, b in enumerate(B):
            if a >= B[-1]:
                break

            if a < b:
                answer += 1
                B.pop(i)
                break
        b_2 = len(B)

        if b_1 == b_2:
            continue

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]), 3)
print(solution([2, 2, 2, 2], [1, 1, 1, 1]), 0)
print(solution([2, 2, 2, 2], [1, 1, 1, 3]), 1)
print(solution([2, 2, 2, 2], [1, 1, 10, 3]), 2)

print(solution([11, 2, 2, 2], [1, 1, 10, 3]), 2)
print(solution([11, 2, 3, 2], [1, 1, 10, 3]), 2)
print(solution([11, 2, 3, 3], [1, 1, 10, 3]), 2)
print(solution([i for i in range(100000)], [i for i in range(100000)]), 99999)
print(solution([100000 for i in range(100000)], [100000 for i in range(100000)]), 99999)
