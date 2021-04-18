# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''

    answer = sorted(numbers, key=lambda number: str(number), reverse=True)
    return answer


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
