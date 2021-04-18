def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [city.lower() for city in cities]

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            if cache and len(cache) >= cacheSize:
                cache.pop()
            answer += 5

        cache.insert(0, city)

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))  # 60
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))  # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
