from collections import deque


def solution(encrypted_text, key, rotation):
    def alphabetToNumber(c):
        return ord(c) - 96
    def numberToAlphabet(n):
        if n < 1:
            #z 인 경우
            if n == 0:
                return 'z'
            return chr(122 - (26 - abs(n % 26)))
        return chr(n + 96)

    answer = deque()
    decryptedText = deque(encrypted_text)
    decryptedText.rotate(-rotation)

    for i in range(len(decryptedText)):
        c = numberToAlphabet(alphabetToNumber(decryptedText[i]) - alphabetToNumber(key[i]))
        answer.append(c)

    return ''.join(answer)


print(solution('abcigoptvfb', 'abddefghijk', 0))  # zellopython
print(solution('qyyigoptvfb', 'abcdefghijk', 3))  # hellopython
# print(solution('hellopython', 'abcdefghijk', 3))  # qyyigoptvfb
