#  input [1, 2, 3]
#  output
#  [1, 2, 3]
#  [1, 3, 2]
#  [2, 1, 3]
#  [2, 3, 1]
#  [3, 1, 2]
#  [3, 2, 1]

prev_elem = []
answer = []


def dfs(elements):
    if len(elements) == 0:
        answer.append(prev_elem[:])

    for elem in elements:
        next_elem = elements[:]
        next_elem.remove(elem)

        prev_elem.append(elem)
        dfs(next_elem)
        prev_elem.pop()

    return answer


print(dfs([1, 2, 3]))
