def solution(names, yearning, photos):
    answer = []
    yearn_dict = dict(map(lambda i, j: (i, j), names, yearning))

    for photo in photos:
        answer.append(sum([yearn_dict[name] for name in photo if name in yearn_dict]))

    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"],
                ["kon", "kain", "may", "coni"]]))  # [19, 15, 6]

print(solution(["kali", "mari", "don"], [11, 1, 55],
               [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))  # [67, 0, 55]

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may"], ["kein", "deny", "may"], ["kon", "coni"]]))  # [5, 15, 0]
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["UNKNOWN"]]))  # [0]
