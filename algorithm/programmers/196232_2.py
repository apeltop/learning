import collections


def solution(people, limit):
    answer = 0
    people.sort()
    d_people = collections.deque(people)

    while d_people:
        person = d_people.pop()
        if d_people and person + d_people[0] <= limit:
            d_people.popleft()

        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3

# def solution(people, limit):
#     def get_max_person(person1):
#         for person2 in people:
#             if limit >= person1 + person2:
#                 return person2
#             return -1
#         return -1
#
#     answer = 0
#
#     people.sort()
#
#     while people:
#         person = people.pop()
#         max_person = get_max_person(person)
#         if not max_person == -1:
#             people.remove(max_person)
#
#         answer += 1
#
#     return answer
