def solution(land):
    answer = 0

    for i, row in enumerate(land):
        max_score = max(row)
        max_index = row.index(max_score)

        if not i == len(land) - 1:
            land[i + 1][max_index] = 0

        answer += max_score

    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16
print(solution([[1, 2, 3, 0], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 15
print(solution([[10, 2, 3, 0], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 22
