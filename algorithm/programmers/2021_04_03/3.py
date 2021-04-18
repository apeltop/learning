import collections


def solution(enroll, referral, seller, amount):
    referDict = {}
    for i in range(len(enroll)):
        referDict[enroll[i]] = referral[i]

    moneyDict = collections.defaultdict(int)

    for i in range(len(seller)):
        sell = amount[i] * 100
        fees = int(sell * 0.1)

        moneyDict[seller[i]] += sell - fees

        refer = referDict[seller[i]]
        while refer != '-':
            moneyDict[refer] += fees - int(fees * 0.1)
            fees = int(fees * 0.1)

            refer = referDict[refer]

    answer = [moneyDict[enroll[i]] for i in range(len(enroll))]
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))  # [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))  # [0, 110, 378, 180, 270, 450, 0, 0]
