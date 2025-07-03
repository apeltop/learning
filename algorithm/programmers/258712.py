# https://school.programmers.co.kr/learn/courses/30/lessons/258712

from collections import defaultdict


def solution(friends, gifts):
    give_dict = defaultdict(dict)
    gift_index = defaultdict(int)

    for gift in gifts:
        a, b = gift.split(" ")
        if b not in give_dict[a]:
            give_dict[a][b] = 1
        else:
            give_dict[a][b] += 1

        gift_index[a] += 1
        gift_index[b] -= 1

    predict_dict = defaultdict(int)

    for friend_a in friends:
        for friend_b in friends:
            if friend_a == friend_b:
                continue

            if friend_b not in give_dict[friend_a]:
                give_dict[friend_a][friend_b] = 0
            if friend_a not in give_dict[friend_b]:
                give_dict[friend_b][friend_a] = 0

            if give_dict[friend_a][friend_b] > give_dict[friend_b][friend_a]:
                predict_dict[friend_a] += 1
            elif give_dict[friend_a][friend_b] == give_dict[friend_b][friend_a]:
                if gift_index[friend_a] > gift_index[friend_b]:
                    predict_dict[friend_a] += 1

    if not predict_dict.items():
        return 0

    return max([v for k, v in predict_dict.items()])


print(solution(["muzi", "ryan", "frodo", "neo"], [
    "muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]),
      2)

print(solution(["joy", "brad", "alessandro", "conan", "david"], [
    "alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]), 4)
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]), 0)
