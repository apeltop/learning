def solution(numbers):
    answer = []

    for number in numbers:
        a_b = '0' + format(number, 'b')

        if a_b[-1] == '0':
            answer.append(number + 1)
            continue

        for i in range(len(a_b) - 1, -1, -1):

            if a_b[i] == '0':
                answer.append(int((a_b[0:i] + '1' + '0' + a_b[i + 2:]), 2))

                if len(a_b) - i > 5:
                    print(a_b, format(number + 1, 'b'), (a_b[0:i] + '1' + '0' + a_b[i + 2:]))
                break

    return answer


print(solution([2, 7]), [3, 11])  # [3, 11]
print(solution([1]), [2])  # [2]
solution([i for i in range(100000)])
print(int('01111011101111111', 2))
# solution([10 ** 15 - i * 5 for i in range(100000)])
# print(solution([10 ** 15 - i * 5 for i in range(100000)]))  # [2]
