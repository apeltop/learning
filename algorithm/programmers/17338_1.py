import collections


def solution(n, delivery):
    answer = ''

    inStockList = [d for d in delivery if d[2] == 1]
    outStockList = [d for d in delivery if d[2] == 0]

    #sku Stock Keeping Unit
    # 1 재고 O
    # 0 재고 ?
    # -1 재고 X

    sku = collections.defaultdict(int)
    for d in inStockList:
        sku[d[0]] = 1
        sku[d[1]] = 1

    for d in outStockList:
        if sku[d[0]] == 1:
            sku[d[1]] = -1
        elif sku[d[1]] == 1:
            sku[d[0]] = -1

    for skuId in range(1, n + 1):
        if sku[skuId] == -1:
            answer += 'X'
        elif sku[skuId] == 0:
            answer += '?'
        elif sku[skuId] == 1:
            answer += 'O'

    return answer


print(solution(6, [[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]]))  # O?O?X?
print(solution(7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))  # O?O?XXO
