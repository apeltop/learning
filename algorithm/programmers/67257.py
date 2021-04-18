# https://programmers.co.kr/learn/courses/30/lessons/67257
import itertools
from collections import deque


def solution(expression):
    answer = 0
    expressionList = []
    operationList = ['-', '+', '*']

    start = 0
    for i in range(len(expression)):
        if expression[i] in operationList:
            expressionList.append(expression[start:i])
            expressionList.append(expression[i])

            start = i + 1
        elif i == len(expression) - 1:
            expressionList.append(expression[start:i + 1])

    for priorityList in itertools.permutations(operationList):
        calculatorList = deque(expressionList[:])
        for priority in priorityList:
            i = 0
            while i < len(calculatorList):
                if calculatorList[i] == priority:
                    r = calculatorList[i+1]
                    o = calculatorList[i]
                    l = calculatorList[i-1]
                    del calculatorList[i+1]
                    del calculatorList[i]
                    del calculatorList[i-1]

                    i -= 1
                    calculatorList.insert(i, eval(f'{l}{o}{r}'))
                else:
                    i += 1
        if answer < abs(calculatorList[0]):
            answer = abs(calculatorList[0])

    return answer


print(solution("100-200*300-500+20"))  # 60420
print(solution("50*6-3*2"))  # 300
print(solution("1+1"))  # 2
