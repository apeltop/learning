# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []

    l, r = 0, 0
    v = sequence[0]
    while r < len(sequence):
        if r < l:
            break

        if v == k:
            if not answer:
                answer = [l, r]
            else:
                if r - l < answer[1] - answer[0]:
                    answer = [l, r]
            v -= sequence[l]
            l += 1
        if v < k:
            if r >= len(sequence) - 1:
                break

            r += 1
            v += sequence[r]
        if v > k:
            v -= sequence[l]
            l += 1


    return answer


print(solution([1], 1))  # [0, 0]
print(solution([1, 2, 3, 4, 5], 7))  # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # [0, 2]
# print(solution([1000 for i in range(1, 1000000)], 1000000000))  # [0, 2]