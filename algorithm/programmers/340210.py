# https://school.programmers.co.kr/learn/courses/30/lessons/340210

def convert_decimal_to_base(decimal_number, base):
    if decimal_number == 0:
        return "0"

    result = []
    decimal_number = abs(decimal_number)

    while decimal_number > 0:
        result.append(str(decimal_number % base))
        decimal_number //= base

    return ''.join(reversed(result))


def convert_base_to_decimal(base_number, base):
    base_number = base_number.lstrip('-')

    decimal_result = 0
    for index, digit in enumerate(reversed(base_number)):
        decimal_result += int(digit) * (base ** index)

    return decimal_result


def solution(expressions):
    answer = []
    possibles = [2, 3, 4, 5, 6, 7, 8, 9]

    known_expressions = [e for e in expressions if e[-1] != 'X']
    unknown_expressions = [e for e in expressions if e[-1] == 'X']

    for expression in expressions:
        expression = expression.replace(' + ', ' ')
        expression = expression.replace(' - ', ' ')
        expression = expression.replace(' = ', ' ')

        n1, n2, n3 = expression.split(' ')

        possibles = [p for p in possibles if p > int(n1[-1])]
        possibles = [p for p in possibles if p > int(n2[-1])]

        if n3 != 'X':
            possibles = [p for p in possibles if p > int(n3[-1])]

    for expression in known_expressions:
        is_negative = '-' in expression

        expression = expression.replace(' + ', ' ')
        expression = expression.replace(' - ', ' ')
        expression = expression.replace(' = ', ' ')

        n1, n2, n3 = expression.split(' ')

        for b in range(possibles[0], 10):
            convert_num1 = int(convert_base_to_decimal(n1, b))
            convert_num2 = int(convert_base_to_decimal(n2, b))
            convert_num2 = convert_num2 * -1 if is_negative else convert_num2

            convert_base_result = convert_decimal_to_base(convert_num1 + convert_num2, b)

            if b in possibles and convert_base_result != n3:
                possibles.remove(b)

    for expression in unknown_expressions:
        result = ''
        ori_expression = expression

        is_negative = '-' in expression
        for p in possibles:

            expression = expression.replace(' + ', ' ')
            expression = expression.replace(' - ', ' ')
            expression = expression.replace(' = ', ' ')

            n1, n2, n3 = expression.split(' ')

            convert_num1 = int(convert_base_to_decimal(n1, p))
            convert_num2 = int(convert_base_to_decimal(n2, p))
            convert_num2 = convert_num2 * -1 if is_negative else convert_num2

            convert_base_result = convert_decimal_to_base(convert_num1 + convert_num2, p)

            if result == '':
                result = convert_base_result
            else:
                if result != convert_base_result:
                    result = '?'

        if result != '?':
            expression = ori_expression.replace('X', result)
        else:
            expression = ori_expression.replace('X', '?')

        answer.append(expression)

    return answer


print(solution(["1 + 1 = 2", "1 + 2 = 3", "1 + 5 = 6", "1 + 3 = X"]), ["1 + 3 = 4"])
print(solution(["1 + 1 = 2", "1 + 2 = 3", "1 + 8 = 10", "1 + 3 = X"]), ["1 + 3 = 4"])
print(solution(["1 + 1 = 2", "1 + 2 = 3", "1 + 3 = X"]), ["1 + 3 = ?"])
print(solution(["8 + 1 = 10", "8 + 1 = X"]), ["8 + 1 = 10"])
# print(solution(["8 + 1 = 10", "8 + 1 = X"]), ["8 + 1 = 10"])
print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]), ["13 - 6 = 5"])
print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]), ["1 + 5 = ?", "1 + 2 = 3"])
print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]),
      ["10 - 2 = 4", "3 + 3 = 10", "33 + 33 = 110"])
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]), ["2 + 2 = 4", "7 + 4 = ?", "5 - 5 = 0"])
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]), ["2 + 2 = 4", "7 + 4 = 12", "8 + 4 = 13"])
