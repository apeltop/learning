# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    dp = [[0, 0] for _ in range(len(sequence))]
    dp[0] = [sequence[0], sequence[0] * -1]

    for i, seq in enumerate(sequence):
        if i == 0:
            continue

        value1, value2 = dp[i - 1][1] + (seq * 1), dp[i - 1][0] + (seq * -1)

        dp[i] = [seq if value1 < seq else value1,
                 seq * -1 if value2 < seq * -1 else value2]

    print(dp)
    return max(map(max, dp))


print(solution([2, 3, -6, 1, 3, -1, 2, 4]), 10)
