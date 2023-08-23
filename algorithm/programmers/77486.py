from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []

    rel_reverse_dict = defaultdict(str)

    income_dict = defaultdict(int)
    for i in range(len(enroll)):
        rel_reverse_dict[enroll[i]] = referral[i] if referral[i] != '-' else 'center'

    for i in range(len(seller)):
        income = amount[i] * 100
        income_target = seller[i]

        net_income, fee = int(income * 0.9), int(income * 0.1)
        while income_target != 'center':
            income_dict[income_target] += net_income
            income_target = rel_reverse_dict[income_target]

            income = fee
            fee = int(fee * 0.1)
            net_income = income - fee

            if income == 0:
                break

            if fee + net_income != income:
                net_income += income - (fee + net_income)

    for e in enroll:
        answer.append(income_dict[e])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]),
      [360, 958, 108, 0, 450, 18, 180, 1080])

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]), [0, 110, 378, 180, 270, 450, 0, 0])
