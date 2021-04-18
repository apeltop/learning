def solution(p, n):
    answer = ""

    t = p.split()[1].split(":")
    total_s = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])

    if p.split()[0] == "PM":
        total_s += 12 * 3600

    total_s += n

    h = str(int(total_s / 3600) % 24)
    m = str(int((total_s % 3600) / 60))
    s = str(int(total_s % 3600 % 60))

    answer = f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}'
    return answer


print(solution("PM 01:00:00", 10))  # 13:00:10
print(solution("PM 11:59:59", 1))  # 00:00:00
print(solution("AM 11:59:59", 1))  # 12:00:00
print(solution("PM 11:59:59", 3600))  # 00:59:59
print(solution("PM 11:59:59", 3601))  # 01:00:00
print(solution("PM 11:59:59", 36000))  # 09:59:59
