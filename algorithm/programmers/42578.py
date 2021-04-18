# https://programmers.co.kr/learn/courses/30/lessons/42578
import collections
import itertools
import math


def solution(clothes):
    answer = 0

    dic = collections.defaultdict(int)

    for cloth in clothes:
        dic[cloth[1]] += 1

    values = dic.values()

    answer += sum(values)

    if len(clothes) == len(values):
        return sum(math.comb(len(clothes), i + 1) for i in range(len(clothes)))

    for i in range(1, len(dic)):
        answer += sum(map(math.prod, itertools.combinations(values, i+1)))

    return answer


print(solution([["yellow_hat", "headgear"], ["yellow_hat", "headgear2"], ["yellow_hat", "headgear3"]]))  # 7
print(solution([["yellow_hat", "headgear"], ["yellow_hat", "headgear2"], ["yellow_hat", "headgear3"], ["yellow_hat", "headgear4"]]))  # 15
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["smoky_makeup", "face"]]))  # 11
print(solution([["yellow_hat", "headgear"]]))  # 1
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
print(solution([
    ["crow_mask", "face"],
    ["crow_mask", "face1"],
    ["crow_mask", "face2"],
    ["crow_mask", "face3"],
    ["crow_mask", "face4"],
    ["crow_mask", "face5"],
    ["crow_mask", "face6"],
    ["crow_mask", "face7"],
    ["crow_mask", "face8"],
    ["crow_mask", "face9"],
    ["crow_mask", "face0"],
    ["crow_mask", "face10"],
    ["crow_mask", "face11"],
    ["crow_mask", "face12"],
    ["crow_mask", "face13"],
    ["crow_mask", "face14"],
    ["crow_mask", "face15"],
    ["crow_mask", "face16"],
    ["crow_mask", "face17"],
    ["crow_mask", "face18"],
    ["crow_mask", "face19"],
    ["crow_mask", "face20"],
    ["crow_mask", "face21"],
    ["crow_mask", "face22"],
    ["crow_mask", "face23"],
    ["crow_mask", "face24"],
    ["crow_mask", "face25"],
    ["crow_mask", "face26"],
    ["crow_mask", "face27"],
    ["crow_mask", "face28"],
    ["crow_mask", "face29"],
    ["crow_mask", "face30"]]))  # 3
