def remove_last_element_zero(arr):
    while arr and arr[-1] == 0:
        arr.pop()
    return arr


def solution(cap, n, deliveries, pickups):
    answer = 0

    def delivery_or_pickup(arr):
        if not arr:
            return
        amount = 0
        while arr and not amount == cap:
            if cap < amount + arr[-1]:
                value = cap - amount
                amount += value
                arr[-1] -= value
                break

            amount += arr[-1]
            arr.pop()

    while deliveries or pickups:
        deliveries = remove_last_element_zero(deliveries)
        pickups = remove_last_element_zero(pickups)

        furthest_delivery_index = max(len(deliveries), len(pickups)) - 1

        delivery_or_pickup(deliveries)
        delivery_or_pickup(pickups)

        answer += (furthest_delivery_index + 1) * 2

    return answer


print(solution(4, 100000, [1 for _ in range(100000)], [1 for _ in range(100000)]), 2500100000)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(2, 7, [0, 0, 0], [0, 0]), 0)
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 0, 0, 0, 0]), 16)
print(solution(4, 5, [1, 0, 3, 0, 0], [0, 3, 0, 4, 0]), 12)
print(solution(1, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 52)
