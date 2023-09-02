def solution(operations):
    answer = []

    q = []
    for operation in operations:
        op, num = operation.split(" ")
        if op == 'I':
            q.append(int(num))
            q.sort()
        if q and op == 'D':
            if num == '1':
                q.pop()
            if num == '-1':
                del q[0]

    return [q[-1], q[0]] if q else [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]), [0, 0])
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]), [333, -45])
