# https://school.programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x), reverse=True)
    phone_book_dict = {phone: True for phone in phone_book}

    for phone in phone_book:
        for l in range(len(phone) - 1):
            if phone[0:l + 1] in phone_book_dict:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]), False)
print(solution(["123", "456", "789"]), True)
print(solution(["12", "123", "1235", "567", "88"]), False)
