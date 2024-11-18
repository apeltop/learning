def solution(name):
    alpha_list = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    def calc_min_alpha_dist(a, b):
        r_cost = 0
        l_cost = 0

        r_a = a
        r_i = alpha_list.index(a)
        while r_a != b:
            r_i += 1
            r_cost += 1

            r_a = alpha_list[r_i]

        l_a = a
        l_i = alpha_list.index(a)
        while l_a != b:
            l_i -= 1
            l_cost += 1

            if l_i == -1:
                l_i = len(alpha_list) - 1

            l_a = alpha_list[l_i]

        return min(r_cost, l_cost)


    start_i = 0
    min_cost = float('inf')
    while start_i < len(name):
        cost = min(start_i, len(name) - start_i)
        cur_name = ['A' for n in name]

        l_i = start_i
        cost += calc_min_alpha_dist(cur_name[l_i], name[l_i])
        cur_name[l_i] = name[l_i]

        while "".join(cur_name) != name:
            l_i -= 1

            if l_i == -1:
                l_i = len(name) - 1

            cost += calc_min_alpha_dist(cur_name[l_i], name[l_i])
            cur_name[l_i] = name[l_i]
            cost += 1

        if cost < min_cost:
            min_cost = cost
        start_i += 1

    start_i = 0
    while start_i < len(name):
        cost = min(start_i, len(name) - start_i)
        cur_name = ['A' for n in name]

        r_i = start_i
        cost += calc_min_alpha_dist(cur_name[r_i], name[r_i])
        cur_name[r_i] = name[r_i]

        while "".join(cur_name) != name:
            r_i += 1

            if r_i == len(name):
                r_i = 0

            cost += calc_min_alpha_dist(cur_name[r_i], name[r_i])
            cur_name[r_i] = name[r_i]
            cost += 1

        if cost < min_cost:
            min_cost = cost
        start_i += 1

    return min_cost


# "JEROEN"	56
# "JAN"	23

print(solution("AAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"), 10)
print(solution("ABBAABAABA"), 12)
print(solution("BB"), 3)
print(solution("DB"), 5)
print(solution("DA"), 3)
print(solution("ADA"), 4)
print(solution("CJAAAAJ"), 23)
print(solution("AAAA"), 0)
print(solution("AAAAABA"), 3)
print(solution("AABAAAA"), 3)
print(solution("JEROEN"), 56)
print(solution("JAN"), 23)
print(solution("JAZ"), 11)
print(solution("AB"), 2)
print(solution("J"), 9)
print(solution("JAJ"), 19)
print(solution("JAAAAJ"), 19)
print(solution("JAAAAJ"), 19)
print(solution("JAAAAJB"), 21)
print(solution("JAAAAJC"), 22)
print(solution("ABAAAAAAABA"), 6)
print(solution("ABBB"), 6)
print(solution("ABBBC"), 9)
print(solution("ADBBC"), 11)
print(solution("CDBBC"), 13)
print(solution("ABAAAAAABA"), 6)
print(solution("ABAAABAABA"), 10)
