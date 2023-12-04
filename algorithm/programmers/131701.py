from collections import defaultdict


def solution(elements):
    answer = 0
    total_s = set()
    sum_dict = defaultdict(set)

    for i in range(1, len(elements) + 1):
        start_i = 0
        end_i = i

        while start_i < len(elements):
            s = sum(elements[start_i:end_i])
            if end_i > len(elements):
                s += sum(elements[0: end_i - len(elements)])
            sum_dict[i].add(s)
            total_s.add(s)
            start_i += 1
            end_i += 1

    return len(total_s)


print(solution([7, 9, 1, 1, 4]), 18)
print(solution([i for i in range(100)]), 18)
print(solution([i for i in range(1000)]), 18)
