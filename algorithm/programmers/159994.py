def solution(cards1, cards2, goal):
    answer = ''

    while cards1 or cards2:
        is_match = False

        if cards1 and goal:
            if cards1[0] == goal[0]:
                is_match = True
                del cards1[0]
                del goal[0]

        if cards2 and goal:
            if cards2[0] == goal[0]:
                is_match = True
                del cards2[0]
                del goal[0]

        if not goal:
            return "Yes"

        if is_match is False:
            return "No"

    return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # "Yes"
print(solution(["i", "drink", "water"], ["want", "to", "a"], ["i", "want", "to", "drink", "water"]))  # "Yes"
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # "No"
