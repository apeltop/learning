#  https://programmers.co.kr/learn/courses/30/lessons/60060

import re


def solution(words, queries):
    answer = []
    queryDic = {}
    wordsLengthDic = {}

    for query in queries:
        if query in queryDic:
            answer.append(queryDic[query])
            continue

        query_length = len(query)
        questionCnt = query.count('?')

        if query[0] == '?':
            wildCard = query[0: questionCnt]
            keyWord = query.replace(wildCard, '')

            keyWord_length = len(keyWord)
            wildCard_length = len(wildCard)
            regex = f'[a-z]{{{wildCard_length}}}{keyWord}$'
        else:
            keyWord = query[0: query_length - questionCnt]
            wildCard = query.replace(keyWord, '')

            keyWord_length = len(keyWord)
            wildCard_length = len(wildCard)
            regex = f'{keyWord}[a-z]{{{wildCard_length}}}$'

        cnt = 0
        for word in words:
            if word not in wordsLengthDic:
                wordsLengthDic[word] = len(word)
            word_length = wordsLengthDic[word]
            
            if not word_length == query_length:
                continue
            if word_length == questionCnt:
                cnt += 1
                continue
            if not query[0] == '?':
                if not keyWord == word[0:keyWord_length]:
                    continue
            else:
                if not keyWord == word[wildCard_length:word_length]:
                    continue

            m = re.compile(regex).match(word)
            if m:
                cnt += 1

        queryDic[query] = cnt
        answer.append(cnt)

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))  # [3, 2, 4, 1, 0]
