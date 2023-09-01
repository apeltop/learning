def solution(order):
    answer = 0
    sub_conveyor = []

    expect_i = 0

    for i in range(1, len(order) + 1):
        if i == order[expect_i]:
            answer += 1
            expect_i += 1

            while sub_conveyor and order[expect_i] == sub_conveyor[-1]:
                answer += 1
                expect_i += 1
                sub_conveyor.pop()
            continue
        elif sub_conveyor and i == sub_conveyor[-1]:
            answer += 1
            expect_i += 1
            sub_conveyor.pop()

            while sub_conveyor and order[expect_i] == sub_conveyor[-1]:
                answer += 1
                expect_i += 1
                sub_conveyor.pop()
            continue

        sub_conveyor.append(i)

    while sub_conveyor and order[expect_i] == sub_conveyor[-1]:
        answer += 1
        expect_i += 1
        sub_conveyor.pop()

    return answer


print(solution([4, 3, 1, 2, 5]), 2)
print(solution([5, 4, 3, 2, 1]), 5)
print(solution([1, 2, 3, 4, 5]), 5)
print(solution([1, 2]), 2)
print(solution([2, 1]), 2)
