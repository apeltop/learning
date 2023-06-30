from collections import defaultdict


def solution(numbers):
    answer = [-1 for _ in numbers]
    wait_list = defaultdict(list)

    prev_value = numbers[0]
    min_value = numbers[0]

    for i, num in enumerate(numbers):
        if min_value < num and num > prev_value:
            for k in list(wait_list.keys()):
                if not k < num:
                    continue

                while wait_list[k]:
                    answer[wait_list[k].pop()] = num
                del wait_list[k]

        if num < min_value:
            min_value = num

        wait_list[num].append(i)
        prev_value = num

    return answer


print(solution([i for i in range(1000000)]))  # [-1, -1, -1]
print(solution([2, 3, 3, 5]))  # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))  # [-1, 5, 6, 6, -1, -1]
print(solution([1, 2, 3]))  # [2, 3, -1]
print(solution([3, 2, 1]))  # [-1, -1, -1]
