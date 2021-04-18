import math
from collections import defaultdict
from collections import deque


def solution(progresses, speeds):
    date_dict = defaultdict(int)

    progresses_q = deque(progresses)
    speeds_q = deque(speeds)

    expect_deploy_date = 0

    while progresses_q:
        progress = progresses_q.popleft()
        speed = speeds_q.popleft()

        estimated_end_time = math.ceil((100 - progress) / speed)
        if expect_deploy_date > estimated_end_time:
            estimated_end_time = expect_deploy_date
        else:
            expect_deploy_date = estimated_end_time

        date_dict[estimated_end_time] += 1

    answer = [k for k in date_dict.values()]

    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
