def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort()
    while A:
        min_a = A.pop()
        max_b = B.pop()

        answer += min_a * max_b

    return answer


print(solution([1, 4, 2], [5, 4, 4]))  # 29
print(solution([1, 2], [3, 4]))  # 10
