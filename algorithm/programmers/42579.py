# https://programmers.co.kr/learn/courses/30/lessons/42579
import collections
import operator


def solution(genres, plays):
    NUM_OF_ADD_LIST = 2
    answer = []

    genresCountByPlays = collections.defaultdict(int)
    genresWithPlays = collections.defaultdict(list)

    for i in range(len(genres)):
        genresCountByPlays[genres[i]] += plays[i]
        genresWithPlays[genres[i]].append((plays[i], i))
        if NUM_OF_ADD_LIST < len(genresWithPlays[genres[i]]):
            genresWithPlays[genres[i]] = sorted(genresWithPlays[genres[i]], key=lambda x: (x[0], -x[1]), reverse=True)[
                                         0:NUM_OF_ADD_LIST]

    for k, v in sorted(genresCountByPlays.items(), key=operator.itemgetter(1), reverse=True):
        for elem in sorted(genresWithPlays[k], key=lambda x: (x[0], -x[1]), reverse=True):
            answer.append(elem[1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", "edm"], [500, 600, 150, 800, 2500, 100]))  # [4, 1, 3, 0, 5]
print(solution(["edm", "classic", "pop", "classic", "classic", "pop"], [100, 500, 600, 150, 800, 2500]))  # [5, 2, 4, 1, 0]
print(solution(["classic", "pop", "classic", "classic", "classic", "pop"], [500, 600, 500, 500, 800, 2500]))  # [5, 1, 4, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 800, 2500]))  # [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
print(solution(["classic"], [500]))  # [0]
print(solution(["classic", "classic"], [500, 500]))  # [0, 1]
