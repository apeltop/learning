# https://programmers.co.kr/learn/courses/30/lessons/42840
import collections


def solution(answers):
    answer = []

    answerSheet = collections.defaultdict(int)

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            answerSheet[1] += 1
        if p2[i % len(p2)] == answers[i]:
            answerSheet[2] += 1
        if p3[i % len(p3)] == answers[i]:
            answerSheet[3] += 1

    most = collections.Counter(answerSheet).most_common(1)

    for k, v in answerSheet.items():
        if v == most[0][1]:
            answer.append(k)

    return sorted(answer)


print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 2, 3, 4, 5, 4]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1,2,3]
