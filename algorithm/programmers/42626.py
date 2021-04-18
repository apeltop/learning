# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    heap = []

    for elem in scoville:
        heapq.heappush(heap, elem)

    while len(heap) > 1 and heap[0] < K:
        low_1 = heapq.heappop(heap)
        low_2 = heapq.heappop(heap)

        mix = low_1 + low_2 * 2

        heapq.heappush(heap, mix)

        answer += 1

    if heap and heap[0] < K:
        answer = -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
