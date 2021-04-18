def solution(n):
    def division_three(ori_n):
        r = ori_n % 3
        return int((ori_n + (0 if r == 0 else 3 - r)) / 3)

    def multiple_three(ori_n):
        r = ori_n % 3
        return int((ori_n + (0 if r == 0 else 3 - r)) * 3)

    def get_threenary(unit_n):
        unit = ''
        r = unit_n % 3
        q = division_three(unit_n)

        if not q == 1:
            unit += get_threenary(q - 1)
        unit += classify[r]
        return unit

    def get_decimal(threenaray):
        unit = ''
        r = threenaray % 3
        q = multiple_three(threenaray)

        if not q == 1:
            unit += get_threenary(q - 1)
        unit += classify[r]
        return unit

    classify = {
        1: '1',
        2: '2',
        0: '0',
    }

    answer = get_threenary(n)
    print(get_decimal(answer))

    return answer


solution(45)  # 7
solution(125)  # 229
