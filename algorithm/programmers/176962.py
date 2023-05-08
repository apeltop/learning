from collections import deque
from datetime import datetime, timedelta


def str_to_time(time_str):
    return datetime.strptime(time_str, "%H:%M")


def calc_plan(plan):
    subject, start_time, duration = plan
    duration = int(duration)

    start_time = str_to_time(plan[1])
    end_time = start_time + timedelta(minutes=duration)

    return start_time, end_time


def is_overlap_plan(plan1, plan2):
    return plan1 > plan2


def solution(plans):
    answer = []

    to_be_plans = deque(sorted(plans.copy(), key=lambda x: x[1]))
    postpone_plans = []
    current_time = None

    while to_be_plans or postpone_plans:
        if not to_be_plans:
            while postpone_plans:
                answer.append(postpone_plans.pop()[0])
            return answer

        if postpone_plans:
            next_start_time = calc_plan(to_be_plans[0])[0]
            if current_time < next_start_time:
                idle_m = int((next_start_time - current_time).seconds / 60)
                if idle_m >= postpone_plans[-1][2]:
                    current_time += timedelta(minutes=postpone_plans[-1][2])
                    answer.append(postpone_plans.pop()[0])
                    continue
                else:
                    postpone_plans[-1][2] -= idle_m

        plan = to_be_plans.popleft()
        start_time, end_time = calc_plan(plan)

        if to_be_plans:
            next_start_time = calc_plan(to_be_plans[0])[0]
            if is_overlap_plan(end_time, next_start_time):
                plan[2] = int(plan[2]) - int((next_start_time - start_time).seconds / 60)
                postpone_plans.append(plan)
                current_time = next_start_time
                continue
        answer.append(plan[0])
        current_time = end_time

    return answer


print(solution(
    [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))  # ["korean", "english", "math"]

print(solution(
    [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"],
     ["computer", "12:30", "100"]]))  # ["science", "history", "computer", "music"]

print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))  # ["bbb", "ccc", "aaa"]

print(solution(
    [["a", "12:20", "40"], ["b", "12:30", "40"], ["c", "12:40", "40"], ["d", "17:00", "10"]]))  # ["c", "b", "a", "d"]
print(solution(
    [["a", "12:20", "40"], ["b", "12:30", "40"], ["c", "12:40", "40"], ["d", "13:20", "10"]]))  # ["c", "d", "b", "a"]
print(solution([["a", "12:20", "10"], ["b", "12:30", "10"], ["c", "12:40", "10"]]))  # ["a", "b", "c"]
print(solution([["c", "12:40", "10"], ["b", "12:30", "10"], ["a", "12:20", "10"]]))  # ["a", "b", "c"]
print(solution([["c", "12:40", "10"], ]))  # ["c"]
print(solution([["a", "12:00", "30"], ["b", "12:10", "30"], ["c", "17:00", "50"]]))  # ["b", "a", "c"]
print(solution([["a", "12:00", "30"], ["b", "12:10", "30"], ["c", "12:20", "30"]]))  # ["c", "b", "a"]
print(solution([["a", "12:00", "1"], ["b", "12:01", "1"], ["c", "12:02", "30"]]))  # ["a", "b", "c"]
print(solution([["a", "01:00", "1"], ["b", "01:01", "1"], ["c", "01:02", "30"]]))  # ["a", "b", "c"]
print(solution([["a", "01:00", "1"], ["c", "01:02", "30"]]))  # ["a", "c"]
print(solution(
    [["a", "12:00", "30"], ["b", "12:10", "60"], ["c", "12:50", "10"]]))  # ["c", "b", "a"]
print(solution(
    [["a", "12:00", "30"], ["b", "12:10", "60"], ["c", "12:50", "10"], ["d", "13:10", "60"]]))  # ["c", "d", "b", "a"]
print(solution(
    [["a", "12:20", "10"], ["b", "12:10", "60"], ["c", "12:40", "10"], ["d", "13:10", "60"]]))  # ["a", "c", "d", "b"]
print(solution(
    [["a", "12:20", "10"], ["b", "12:10", "60"], ["c", "12:40", "10"], ["d", "14:10", "60"]]))  # ["a", "c", "b", "d"]
