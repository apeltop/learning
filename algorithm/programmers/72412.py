from bisect import bisect_left
from collections import defaultdict


def solution(infos, queries):
    answer = []

    info_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    scores_dict = defaultdict(list)

    select_dict = {
        0: [['java'], ['cpp'], ['python']],
        1: [['backend'], ['frontend']],
        2: [['junior'], ['senior']],
        3: [['chicken'], ['pizza']]
    }

    for info in infos:
        chunks = info.split(" ")
        info_dict[chunks[0]][chunks[1]][chunks[2]][chunks[3]].append(int(chunks[4]))

    for query in queries:
        query = [chunk for chunk in query.split(" ") if chunk != 'and']
        search = []

        for i, q in enumerate(query):
            arr = []

            if q != '-':
                if not search:
                    search = [[q]]
                    continue

                for s in search:
                    arr.append(s + [q])

            if q == '-':
                if i == 0 and not search:
                    arr = select_dict[0]
                else:
                    for s in search:
                        for select in select_dict[i]:
                            arr.append(s + select)

            search = arr

        scores = []

        if ''.join(query[0:4]) in scores_dict:
            scores = scores_dict[''.join(query[0:4])]

        if not scores:
            for s in search:
                scores.extend(info_dict[s[0]][s[1]][s[2]][s[3]])

        scores = scores if ''.join(query[0:4]) in scores_dict else sorted(scores)
        count = len(scores) - bisect_left(scores, int(search[0][4]))

        if ''.join(query[0:4]) not in scores_dict:
            scores_dict[''.join(query[0:4])] = scores
        answer.append(count)

    return answer


# print(solution(
#     ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
#      "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
#         "- and - and - and - 150"]), [1, 1, 1, 1, 2, 4])

info = ["java backend junior pizza 150" for i in range(50000)]
query = ["- and - and - and - 150" for i in range(100000)]

print(solution(info, query))

print(solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]), [1, 1, 1, 1, 2, 4])
