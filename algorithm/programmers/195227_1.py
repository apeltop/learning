def solution(arr):
    answer = []

    for elem in arr:
        if len(answer) == 0 or not elem == answer[-1]:
            answer.append(elem)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1,3,0,1]
print(solution([4, 4, 4, 3, 3]))  # [4,3]
