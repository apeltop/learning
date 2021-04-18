# https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        essential_skill = "".join([essential for essential in list(skill_tree) if essential in skill])
        if essential_skill == skill[0:len(essential_skill)]:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))  # 2
