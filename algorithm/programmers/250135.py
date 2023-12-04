def calc_clock_angle(h, m, s):
    second_angle = 6 * s
    minute_angle = 6 * m + (s / 10)
    hour_angle = (30 * h + m * 0.5 + (s * (0.5 / 60))) % 360

    return hour_angle, minute_angle, second_angle


def increase_s(cur_h, cur_m, cur_s):
    cur_s += 1
    if cur_s == 60:
        cur_m += 1
        cur_s = 0

    if cur_m == 60:
        cur_h += 1
        cur_m = 0
    return cur_h, cur_m, cur_s


def decrease_s(cur_h, cur_m, cur_s):
    cur_s -= 1
    if cur_s < 0:
        cur_s = 59
        cur_m -= 1

    if cur_m < 0:
        cur_m = 59
        cur_h -= 1

    if cur_h < 0:
        cur_h = 23

    return cur_h, cur_m, cur_s


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    clock_angles = []

    cur_h, cur_m, cur_s = h1, m1, s1
    h2, m2, s2 = increase_s(h2, m2, s2)

    while not (cur_h >= h2 and cur_m >= m2 and cur_s >= s2):
        clock_angles.append(((cur_h % 12, cur_m, cur_s), calc_clock_angle(cur_h % 12, cur_m, cur_s)))
        cur_h, cur_m, cur_s = increase_s(cur_h, cur_m, cur_s)

    for i, angle_info in enumerate(clock_angles):
        hms, angles = angle_info

        h_angle, m_angle, s_angle = angles
        if h_angle == 0 and m_angle == 0 and s_angle == 0:
            answer += 1
            continue

        if m_angle == s_angle:
            answer += 1

        if i == 0:
            continue

        before_s_angle = clock_angles[i - 1][1][2]
        if before_s_angle < h_angle < s_angle:
            answer += 1
            if hms[1] == 0 and hms[2] == 1:
                answer -= 1

        elif before_s_angle == 354 and before_s_angle < h_angle < 360:
            answer += 1

        if before_s_angle < m_angle < s_angle:
            answer += 1
            if hms[1] == 0 and hms[2] == 1:
                answer -= 1

        elif before_s_angle == 354 and before_s_angle < m_angle < 360:
            answer += 1

    return answer


print(solution(0, 0, 0, 23, 59, 59), 2852)

print(solution(23, 59, 58, 23, 59, 59), 0)
print(solution(23, 59, 57, 23, 59, 59), 0)

print(solution(0, 58, 59, 0, 59, 1), 0)
print(solution(0, 58, 58, 0, 59, 1), 1)

print(solution(12, 0, 0, 12, 1, 1), 2)

print(solution(12, 0, 0, 12, 0, 30), 1)
print(solution(0, 5, 59, 0, 7, 0), 2)
print(solution(0, 5, 30, 0, 7, 0), 2)

print(solution(12, 0, 58, 12, 1, 1), 1)

print(solution(12, 0, 0, 12, 0, 30), 1)
print(solution(12, 0, 0, 12, 0, 59), 1)
print(solution(11, 58, 0, 11, 59, 0), 2)
print(solution(12, 58, 00, 12, 59, 0), 2)
print(solution(12, 58, 00, 12, 59, 5), 3)

print(solution(12, 00, 1, 12, 1, 1), 1)
print(solution(12, 00, 1, 12, 1, 2), 2)

print(solution(0, 5, 59, 0, 7, 0), 2)
print(solution(0, 5, 30, 0, 7, 0), 2)
print(solution(0, 5, 30, 0, 7, 1), 3)
print(solution(0, 5, 30, 0, 7, 2), 3)

print(solution(0, 6, 1, 0, 6, 6), 0)
print(solution(11, 59, 59, 12, 0, 0), 1)
print(solution(12, 00, 0, 12, 0, 1), 1)
print(solution(12, 00, 1, 12, 0, 2), 0)
print(solution(12, 00, 1, 12, 0, 59), 0)
print(solution(12, 00, 1, 12, 1, 0), 0)
print(solution(11, 59, 59, 12, 0, 30), 1)

print(solution(0, 0, 0, 11, 59, 59), 1426)
print(solution(0, 0, 0, 0, 0, 30), 1)
print(solution(1, 5, 5, 1, 5, 6), 2)
print(solution(11, 59, 30, 12, 0, 0), 1)

print(solution(0, 5, 30, 0, 7, 0), 2)
print(solution(12, 0, 0, 12, 0, 30), 1)
print(solution(0, 6, 1, 0, 6, 6), 0)
print(solution(11, 59, 30, 12, 0, 0), 1)
print(solution(11, 58, 59, 11, 59, 0), 1)
print(solution(1, 5, 5, 1, 5, 6), 2)
print(solution(0, 0, 0, 23, 59, 59), 2852)
print(solution(0, 0, 0, 12, 0, 0), 1427)

print(solution(0, 0, 0, 0, 0, 1), 1)
print(solution(12, 0, 0, 23, 59, 59), 1426)
