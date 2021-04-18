# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    countByTransform = countByZero = 0

    while s != "1":
        zero = s.count("0")
        s = str(bin(len(s) - zero))[2:]

        countByZero += zero
        countByTransform += 1

    return [countByTransform, countByZero]


print(solution("110010101001"))  # [3,8]
print(solution("01110"))  # [3,3]
print(solution("1111111"))  # [4,1]
