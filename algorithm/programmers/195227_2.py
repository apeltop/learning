def solution(arr, divisor):
    answer = sorted([elem for elem in arr if elem % divisor == 0])
    if not answer:
        answer.append(-1)
    return answer


print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
print(solution([3, 2, 6], 10))  # [-1]
