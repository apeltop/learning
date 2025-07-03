# https://school.programmers.co.kr/learn/courses/30/lessons/12906
#

def solution(arr):
    answer = []

    for a in arr:
        if not answer:
            answer.append(a)
            continue

        if answer[-1] == a:
            continue

        answer.append(a)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]), [1, 3, 0, 1])
print(solution([4, 4, 4, 3, 3]), [4, 3])
