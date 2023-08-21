from collections import deque


def solution(queue1, queue2):
    answer = 0

    l_sum = sum(queue1)
    r_sum = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    if (l_sum + r_sum) % 2 == 1:
        return -1

    while l_sum != r_sum:
        if answer > (len(queue1) + len(queue2)) * 2:
            return -1

        if l_sum < r_sum:
            elem = queue2.popleft()
            queue1.append(elem)

            l_sum += elem
            r_sum -= elem
        else:
            elem = queue1.popleft()
            queue2.append(elem)

            l_sum -= elem
            r_sum += elem

        if not queue1 or not queue2:
            return -1

        answer += 1

    return answer


print(solution([1, 2], [1, 1]), -1)
print(solution([3, 2, 7, 2], [4, 6, 5, 1]), 2)
print(solution([1, 2, 1, 2], [1, 10, 1, 2]), 7)
print(solution([1, 1], [1, 5]), -1)
print(solution([i for i in range(300000)], [i for i in range(300000 - 16)]), -1)
