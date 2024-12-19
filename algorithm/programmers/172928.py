# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    y, x = next((y, x) for y, row in enumerate(park) for x, col in enumerate(park[y]) if park[y][x] == 'S')
    for route in routes:
        command, v = route.split(" ")
        v = int(v)

        ny, nx = y, x
        if command == 'E':
            nx += v
        elif command == 'W':
            nx -= v
        elif command == 'S':
            ny += v
        elif command == 'N':
            ny -= v

        if not ((0 <= ny < len(park)) and (0 <= nx < len(park[0]))):
            continue

        if command in 'EW':
            x1, x2 = sorted([x, nx])
            if 'X' in park[ny][x1:x2 + 1]:
                continue
        elif command in 'SN':
            y1, y2 = sorted([y, ny])
            if any([v for v in park[y1:y2 + 1] if v[nx] == 'X']):
                continue
        y, x = ny, nx

    return [y, x]


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]), [2, 1])
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]), [0, 1])
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]), [0, 0])
