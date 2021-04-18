import collections


def solution(votes, k):
    answer = ''
    counts = collections.Counter(sorted(votes)).most_common()
    top2_vote = 0
    for i in range(k):
        top2_vote += counts[i][1]
    drop_vote = 0

    while counts:
        car_vote = counts.pop()
        if top2_vote <= car_vote[1] + drop_vote:
            break
        answer = car_vote[0]
        drop_vote += car_vote[1]

    return answer


print(solution(
    ["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND",
     "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))  # RAIN
print(solution(["AAD", "AAA", "AAC", "AAB"], 4))  # AAB
