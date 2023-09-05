from collections import defaultdict


def solution(want, number, discount):
    answer = 0

    expect_cart_dict = {want[i]: number[i] for i in range(len(want))}
    current_cart_dict = defaultdict(int)

    for i in range(len(discount)):
        item = discount[i]
        current_cart_dict[item] += 1

        is_expect = True
        for k in expect_cart_dict.keys():
            if k not in current_cart_dict:
                is_expect = False
                break

            if current_cart_dict[k] < expect_cart_dict[k]:
                is_expect = False
                break

        if is_expect:
            answer += 1

        if sum(current_cart_dict.values()) == 10:
            current_cart_dict[discount[i - 9]] -= 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], [
    "chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple",
    "banana"]),
      3)

print(solution(
    ["apple"], [10],
    ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]),
    0)
