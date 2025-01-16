def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], x[1]))

    l, r = routes[0]
    answer += 1
    for route in routes[1:]:
        if route[0] <= r:
            r = min(r, route[1])
            continue

        l, r = route
        answer += 1

    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]), 2)
print(solution([[-20, -2], [-14, -5], [-18, -5], [-5, -5]]), 1)
print(solution([[-20, -15], [-5, -3]]), 2)
