def is_valid_parentheses(expression):
    stack = []
    for s in expression:
        if s == '[' or s == '(' or s == '{':
            stack.append(s)
            continue

        if not stack:
            return False
        if s == ']':
            if not '[' == stack.pop():
                return False
        if s == ')':
            if not '(' == stack.pop():
                return False
        if s == '}':
            if not '{' == stack.pop():
                return False

    return False if stack else True


def solution(s):
    answer = 0

    for i in range(len(s)):
        s = s[1:] + s[0]
        answer += 1 if is_valid_parentheses(s) else 0

    return answer


print(solution("[](){}"), 3)
print(solution("}]()[{"), 2)
print(solution("[)(]"), 0)
print(solution("}}}"), 0)
