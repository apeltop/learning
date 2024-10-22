# https://school.programmers.co.kr/learn/courses/30/lessons/340213?language=python3
def convert_to_seconds(mm_ss: str):
    mm, ss = mm_ss.split(":")

    total_s = int(ss) + int(mm) * 60
    return total_s

def convert_to_mm_ss(seconds):
    mm, ss = divmod(seconds, 60)
    mm = str(mm).zfill(2)
    ss = str(ss).zfill(2)

    return f'{mm}:{ss}'

# print(convert_to_seconds("10:55"))
# print(convert_to_mm_ss(convert_to_seconds("10:55")))

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len_s = convert_to_seconds(video_len)
    pos_s = convert_to_seconds(pos)
    op_start_s = convert_to_seconds(op_start)
    op_start_e = convert_to_seconds(op_end)

    for command in commands:
        if op_start_s <= pos_s < op_start_e:
            pos_s = op_start_e

        if command == 'next':
            pos_s = min(pos_s + 10, video_len_s)
        if command == 'prev':
            pos_s = max(0, pos_s - 10)

        if op_start_s <= pos_s < op_start_e:
            pos_s = op_start_e

    return convert_to_mm_ss(pos_s)


# print()
print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]), "13:00")
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]), "06:55")
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]), "04:17")
