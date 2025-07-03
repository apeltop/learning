# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    for size in [size for size in sizes if size[0] < size[1]]:
        size[0], size[1] = size[1], size[0]

    return max([size[0] for size in sizes]) * max([size[1] for size in sizes])


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]), 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]), 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]), 133)
