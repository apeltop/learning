def solution(n, left, right):
    answer = []

    def calc_value(row, col):
        return max(row, col) + 1

    for i in range(left, right + 1):
        answer.append(calc_value(i // n, i % n))

    return answer


print(solution(3, 2, 5), [3, 2, 2, 3])
print(solution(4, 7, 14), [4, 3, 3, 3, 4, 4, 4, 4])
