# https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    def compress(y, x, k):
        rect = []
        for i in range(int(k)):
            for j in range(int(k)):
                rect.append(arr[y + i][x + j])
        rect.sort()
        isSameValue = rect[0] == rect[-1]

        if isSameValue:
            if rect[0] == 0:
                return [1, 0]
            if rect[0] == 1:
                return [0, 1]

        v = compress(y, x, int(k / 2)) \
            + compress(y, x + int(k / 2), int(k / 2)) \
            + compress(y + int(k / 2), x, int(k / 2)) \
            + compress(y + int(k / 2), x + int(k / 2), int(k / 2))

        z = sum([v[i] for i in range(len(v)) if i % 2 == 0])
        o = sum([v[i] for i in range(len(v)) if i % 2 == 1])

        return [z, o]
    return compress(0, 0, len(arr))


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))  # [4,9]
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))  # [10,15]
