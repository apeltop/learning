import collections


def solution(lottos, win_nums):
    dic = collections.defaultdict(bool)
    for num in win_nums:
        dic[num] = False

    for num in lottos:
        if num in dic:
            dic[num] = True

    prizeDict = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    mini = len([k for k, v in dic.items() if dic[k]])
    maxi = mini + len([num for num in lottos if num == 0])

    return [prizeDict[maxi], prizeDict[mini]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
