def solution(schedules, timelogs, startday):
    late_set = set()
    for i, schedule in enumerate(schedules):
        schedule += 10

        h, m = schedule // 100, schedule % 100

        if schedule % 100 >= 60:
            h += 1
            m -= 60
        schedules[i] = h * 100 + m

    for i in range(len(timelogs[0])):
        today = (startday - 1 + i) % 7 + 1
        if today in (6, 7):
            continue

        for s_i, schedule in enumerate(schedules):
            if schedule < timelogs[s_i][i]:
                late_set.add(s_i)

    return len(schedules) - len(late_set)


# print(solution([700], [[611]], 1), 0)
# print(solution([750], [[611]], 1), 0)
# print(solution([759], [[611]], 1), 0)
# print(solution([749], [[611]], 1), 0)
# print(solution([600], [[611]], 1), 0)
# print(solution([600], [[20]], 1), 1)
# print(solution([30], [[20]], 1), 1)
# print(solution([30], [[20]], 1), 1)
# print(solution([759], [[912]], 8), 0)
# print(solution([730], [[700, 912]], 6), 1)
# print(solution([730], [[931, 912]], 6), 1)
# print(solution([730], [[912]], 7), 1)
# print(solution([730], [[912]], 7), 1)
# print(solution([730], [[710, 700, 650, 735, 700, 931, 912]], 6), 0)

print(solution([750, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809],
                                  [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5), 3)

print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809],
                                  [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5), 3)
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835],
                                      [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1), 2)
# print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835],
#                                       [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 7), 7)
