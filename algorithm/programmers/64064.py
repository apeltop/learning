# https://programmers.co.kr/learn/courses/30/lessons/64064
import itertools
import re


def solution(user_id, banned_id):
    answer = []
    possibleBanUser = []

    for user in user_id:
        for ban in banned_id:
            p = re.compile(ban.replace('*', '.'))
            m = p.match(user)
            if m and m.group() == user:
                possibleBanUser.append(user)
                break

    banList = []
    for userList in itertools.permutations(possibleBanUser):
        banUserList = []
        for ban in banned_id:
            for user in userList:
                p = re.compile(ban.replace('*', '.'))
                m = p.match(user)
                if m and m.group() == user and user not in banUserList:
                    banUserList.append(user)
                    break
        if banUserList and len(banUserList) >= len(banned_id):
            banList.append(sorted(banUserList))

    for ban in sorted(banList):
        if ban not in answer:
            answer.append(ban)

    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))  # 3
print(solution(["abcdee", "abcdef", "abcdea", "abcdeb"], ["******", "******", "******"]))  # 4
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "*****", "******", "******"]))  # 1
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc", "a"], ["fr*d*", "abc1**", "*", "*"]))  # 0
print(solution(["frodoc", "abcdef"], ["******", "******", "******"]))  # 0
print(solution(["frodoc", "abcdef"], ["******"]))  # 2
print(solution(["frodoc1", "abcdef"], ["******1"]))  # 1
print(solution(["a", "b"], ["*", "*", "*"]))  # 0
print(solution(["b", "a"], ["*", "*", "*"]))  # 0
print(solution(["frodo"], ["******", "******"]))  # 0
print(solution(["123456"], ["******", "******"]))  # 0
