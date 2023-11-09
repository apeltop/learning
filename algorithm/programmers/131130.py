from collections import defaultdict


def solution(cards):
    answer = 0

    boxs_dict = defaultdict(int)
    for i, card in enumerate(cards):
        boxs_dict[i + 1] = card

    linked_cards = []
    for i in range(1, len(cards) + 1):
        box_i = i
        linked_card = []
        while boxs_dict[box_i] not in linked_card:
            linked_card.append(boxs_dict[box_i])
            box_i = boxs_dict[box_i]
        linked_card = sorted(linked_card)

        if linked_card not in linked_cards:
            linked_cards.append(linked_card)

    linked_cards.sort(key=len)

    return 0 if len(linked_cards) < 2 else len(linked_cards[-1]) * len(linked_cards[-2])


print(solution([1, 2]))  # 8
print(solution([6, 3, 7, 2, 5, 1, 4]))  # 8
print(solution([8, 6, 3, 7, 2, 5, 1, 4]))  # 12
