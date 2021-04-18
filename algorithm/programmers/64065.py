# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []

    elements = []
    s = s[1:-1].replace('{', '').replace('},', '}')
    setElement = []
    element = ''
    for i in range(len(s)):
        if s[i] == '}':
            setElement.append(int(element))
            element = ''

            elements.append(setElement)
            setElement = []
        elif s[i].isdigit():
            element += s[i]
        else:
            setElement.append(int(element))
            element = ''

    elements.sort(key=lambda x: len(x))

    for setElem in elements:
        for elem in setElem:
            if elem not in answer:
                answer.append(elem)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]
