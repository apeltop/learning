# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3

def solution(t, p):
    answer = 0
    for i, a in enumerate(t):
        sub_str = t[i:i+len(p)]
        if(len(sub_str)) != len(p):
            break
        answer += 1 if sub_str <= p else 0
    return answer


print(solution("3141592", "271"))  # 2
print(solution("500220839878", "7"))  # 8
print(solution("10203", "15"))  # 3
