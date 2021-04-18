# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    h = []
    taskTime = currentTime = 0
    jobs.sort()
    i = 0
    while i < len(jobs):
        if jobs[i][0] < currentTime:
            heapq.heappush(h, [jobs[i][1], jobs[i][0]])
        else:
            while h:
                if jobs[i][0] < currentTime:
                    break
                needTime, requestTime = heapq.heappop(h)
                if currentTime < requestTime:
                    currentTime = requestTime
                    taskTime += needTime
                else:
                    currentTime += needTime
                    taskTime += currentTime - requestTime

            if jobs[i][0] < currentTime:
                continue
            if currentTime < jobs[i][0]:
                currentTime = jobs[i][0] + jobs[i][1]
                taskTime += jobs[i][1]
            else:
                currentTime += jobs[i][1]
                taskTime += currentTime - jobs[i][0]
        i += 1

    while h:
        needTime, requestTime = heapq.heappop(h)

        if currentTime < requestTime:
            currentTime = requestTime
            taskTime += needTime
        else:
            currentTime += needTime
            taskTime += currentTime - requestTime

    return int(taskTime / len(jobs))


print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))  # 15
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))  # 72
print(solution([[0, 3], [6, 1], [4, 1]]))  # 1
print(solution([[0, 3], [1, 9], [2, 6], [19, 2]]))  # 7
print(solution([[2, 6], [19, 2], [0, 3], [1, 9]]))  # 7
print(solution([[0, 3], [2, 6], [1, 9]]))  # 9
print(solution([[0, 3]]))  # 3
