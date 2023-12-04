def solution(n, l, r):
    answer = 0

    cantor_size = 5 ** n
    parts_size = cantor_size / 5

    one_by_l = [1, 4, 3, 2, 2][l % 5]
    one_by_r = [4, 1, 2, 2, 3][r % 5]

    if n == 1:
        return '11011'[l - 1:r].count('1')

    def calc_1_count(start, end):
        start, end = int(start), int(end)
        interval = end - start

        if start >= r or end < l:
            return 0

        if interval == 5:
            if not (start < l <= end or start < r <= end):
                return 4

            if l == r:
                return 0 if l % 5 == 3 else 1

            if start < l <= end:
                total_1 = one_by_l

                if start < r <= end:
                    total_1 -= one_by_r
                return total_1

            if start < r <= end:
                return one_by_r

            return 0

        return sum(
            [calc_1_count(start + (interval / 5 * i), start + interval / 5 * (i + 1)) for i in [0, 1, 3, 4]]
        )

    for i in [0, 1, 3, 4]:
        answer += calc_1_count((parts_size * i), parts_size * (i + 1))

    return answer


# def solution(n, l, r):
#     answer = 0
#
#     BIT_0 = '00000'
#     BIT_1 = '11011'
#
#     cantor_dict = defaultdict(str)
#     cantor_dict[1] = BIT_1
#
#     for i in range(2, n + 1):
#         # if r <= len(cantor_dict[i - 1]):
#         #     return cantor_dict[i - 1][l - 1:r].count('1')
#
#         cantor_dict[i] = cantor_dict[i - 1] + cantor_dict[i - 1] + BIT_0 * (5 ** (i - 2)) + cantor_dict[i - 1] + \
#                          cantor_dict[i - 1]
#
#         # print(cantor_dict[i])
#         print(cantor_dict[i].count('0'), cantor_dict[i].count('1'), sys.getsizeof(cantor_dict[i]))
#
#     return cantor_dict[n][l - 1:r].count('1')


print(solution(2, 1, 1), 1)
print(solution(2, 3, 3), 0)
print(solution(3, 1, 120), 60)
print(solution(3, 6, 125), 60)
print(solution(3, 5, 125), 61)
print(solution(3, 4, 125), 62)
print(solution(1, 1, 1), 1)
print(solution(1, 1, 2), 2)
print(solution(1, 1, 3), 2)
print(solution(1, 1, 4), 3)
print(solution(1, 1, 5), 4)
print(solution(2, 1, 2), 2)
print(solution(2, 20, 25), 5)
print(solution(2, 1, 3), 2)
print(solution(2, 1, 25), 16)
print(solution(2, 24, 3), 0)
print(solution(2, 4, 17), 8)
print(solution(3, 4, 17), 8)
print(solution(3, 1, 124), 63)
print(solution(3, 2, 124), 62)
print(solution(3, 1, 125), 64)
print(solution(3, 3, 125), 62)
print(solution(3, 1, 121), 61)
print(solution(15, 4, 17), 8)
# print(solution(20, 4, 17))  # 8
# print(solution(20, 4, 4 + 10000000))  # 418381822

# 9 16 74
# 61 64 174
# 369 256 674
# 2101 1024 3174
# 11529 4096 15674
# 61741 16384 78174
# 325089 65536 390674
# 1690981 262144 1953174
# 8717049 1048576 9765674
# 44633821 4194304 48828174
# 227363409 16777216 244140674
# 1153594261 67108864 1220703174
# 5835080169 268435456 6103515674
# 29443836301 1073741824 30517578174
