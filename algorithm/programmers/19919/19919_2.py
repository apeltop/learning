import collections
import itertools


def isValid(s):
    stack = []
    table = {
        ')': '(',
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


def solution(arr1, arr2):
    answer = -1

    validB1 = [a for a in arr1 if isValid(a)]
    validB2 = [a for a in arr2 if isValid(a)]
    inValidB1 = [a for a in arr1 if not isValid(a)]
    inValidB2 = [a for a in arr2 if not isValid(a)]

    inValidDict1 = collections.defaultdict(list)
    for v in inValidB1:
        while '()' in v:
            v = v.replace('()', '')
        inValidDict1[v].append(v)

    inValidDict2 = collections.defaultdict(list)
    for v in inValidB2:
        newExp = ''
        # while '()' in v:
        #     v = v.replace('()', '')

        for i in range(len(v)):
            if v[i] == '(':
                newExp += ')'
            elif v[i] == ')':
                newExp += '('
        inValidDict2[newExp[::-1]].append(newExp)

    if validB1 and validB2:
        answer = len(validB1) * len(validB2)

    for k, v in inValidDict1.items():
        l = inValidDict2[k]
        answer += len(v) * len(l)

    return answer


print(solution(["())"], [")()", "()", "(()"]))  # -1
print(solution(["()"], [")()", "(()"]))  # -1
print(solution(["("], [")()", ")"]))  # 2
print(solution(["()"], [")()", "()", "(()"]))  # 1
print(solution(["()", "("], [")()", "()", "(()"]))  # 2
print(solution(["()", "(()", ")()", "()"], [")()", "()", "(()"]))  # 3
print(solution(["()", "(()", "(", "(())"], [")()", "()", "(())", ")()"]))  # 8
