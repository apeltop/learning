# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0

    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    counts = []
    for i in range(row_begin - 1, row_end):
        row = sorted_data[i]

        mod_sum = 0
        for j in range(len(row)):
            mod_sum += row[j] % (i + 1)
        counts.append(mod_sum)

    answer = counts[0]
    for i, elem in enumerate(counts[1::]):
        answer = answer ^ elem
    return answer


# Sorted Arr ->  {4, 2, 9}, {2, 2, 6}, {1, 5, 10}, {3, 8, 3}

# S_2 = (2 mod 2) + (2 mod 2) + (6 mod 2) = 0 입니다.
# S_3 = (1 mod 3) + (5 mod 3) + (10 mod 3) = 4 입니다.

print(solution([[2, 2, 6, 1], [1, 5, 10, 1], [4, 2, 9, 1], [3, 8, 3, 1]], 2, 2, 3))  # 4
print(solution([[2, 2, 6], [4, 2, 9], [3, 8, 3]], 2, 2, 3))  # 2
print(solution([[2, 2, 6]], 1, 1, 1))  # 0
print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))  # 4
print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9]], 2, 2, 3))  # 4
