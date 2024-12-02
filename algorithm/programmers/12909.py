# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = []

    for a in s:
        if a == "(":
            stack.append(a)
        if a == ")":
            if not stack:
                return False
            if stack[-1] != "(":
                return False
            stack.pop()

    return len(stack) == 0


print(solution("()()"), True)
print(solution("(())()"), True)
print(solution(")()("), False)
print(solution("(()("), False)
