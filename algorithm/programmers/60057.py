# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    minimumStr = s

    for i in range(1, int(len(s) / 2) + 1):
        compressStr = ''
        curIndex = 0
        while curIndex < len(s):
            duplCount = 1
            while s[curIndex:curIndex + i] == s[curIndex + duplCount * i:curIndex + (duplCount + 1) * i]:
                duplCount += 1

            if not duplCount == 1:
                compressStr += f'{duplCount}'
            compressStr += f'{s[curIndex:curIndex + i]}'

            curIndex += duplCount * i
        if len(minimumStr) > len(compressStr):
            minimumStr = compressStr

    return len(minimumStr)


print(solution("aabbaccc"))  # 7
print(solution("ababcdcdababcdcd"))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
