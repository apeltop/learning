def solution(S):
    stack = []
    op = S.split(' ')

    i = 0
    while i < len(op):
        if op[i].isdigit():
            stack.append(int(op[i]))
        elif op[i] == 'DUP':
            stack.append(stack[-1])
        elif op[i] == 'POP':
            if not stack:
                return -1

            stack.pop()
        elif op[i] == '+' or '-':
            if len(stack) < 2:
                return -1
            a, b = stack[-1], stack[-2]
            r = 0
            try:
                if op[i] == '+':
                    r = a + b
                elif op[i] == '-':
                    r = a - b
            except OverflowError as err:
                print(f'{err} {a} + {b}')
                return -1
            stack.pop()
            stack.pop()
            stack.append(r)

        i += 1
    return stack[-1]


print(solution("5 6 + -"))
print(solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(solution("POP DUP 4 POP 5 DUP + DUP + -"))
