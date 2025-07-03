# https://school.programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    min_count = 0
    max_count = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            max_count += 1
        elif lottos[i] in win_nums:
            max_count += 1
            min_count += 1

    def calc_prize(match_count):
        return 6 if match_count < 2 else  7 - match_count

    return [calc_prize(max_count), calc_prize(min_count)]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]), [3, 5])
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]), [1, 6])
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]), [1, 1])
