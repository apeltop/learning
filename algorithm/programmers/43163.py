# https://programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    def isTypo(original_word, typo_word):
        flag = True
        for i in range(len(original_word)):
            if not original_word[i] == typo_word[i]:
                if not flag:
                    return False
                flag = False
        return True

    answer = []

    def dfs(typo, next_words):
        if typo == target:
            answer.append(prev_elem[:])
            return

        for word in next_words:
            next_elem = next_words[:]
            if isTypo(typo, word):
                prev_elem.append(word)
                next_elem.remove(word)
                dfs(word, next_elem)
                prev_elem.remove(word)

        return

    prev_elem = []
    dfs(begin, words)

    if not answer:
        return 0
    return len(min(answer))


print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))  # 4 hit -> hot -> dot -> dog -> cog
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))  # 0
