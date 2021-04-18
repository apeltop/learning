import collections
from collections import deque


class Node:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.n3 = None
        self.n4 = None


def solution(S1, S2):
    answer = 0
    S1 = deque(S1)
    S2 = deque(S2)

    tree = Node()

    cur_node = tree
    cur_level = 0
    indexDict = collections.defaultdict(int)

    while S1:
        if S1[0] == 'p':
            if indexDict[cur_level] == 0:
                cur_node.n1 = Node()
                cur_node = cur_node.n1
            elif indexDict[cur_level] == 1:
                cur_node.n2 = Node()
                cur_node = cur_node.n2
            elif indexDict[cur_level] == 2:
                cur_node.n3 = Node()
                cur_node = cur_node.n3
            elif indexDict[cur_level] == 3:
                cur_node.n4 = Node()
                cur_node = cur_node.n4

            cur_level += 1

        elif S1[0] == 'w':
            if indexDict[cur_level] == 0:
                cur_node.n1 = 'w'
            elif indexDict[cur_level] == 1:
                cur_node.n2 = 'w'
            elif indexDict[cur_level] == 2:
                cur_node.n3 = 'w'
            elif indexDict[cur_level] == 3:
                cur_node.n4 = 'w'

        elif S1[0] == 'b':
            if indexDict[cur_level] == 0:
                cur_node.n1 = 'b'
            elif indexDict[cur_level] == 1:
                cur_node.n2 = 'b'
            elif indexDict[cur_level] == 2:
                cur_node.n3 = 'b'
            elif indexDict[cur_level] == 3:
                cur_node.n4 = 'b'

        if S1[0] == 'p':
            indexDict[cur_level] = 0
        else:
            if indexDict[cur_level] == 3:
                indexDict[cur_level] = 0
                cur_level -= 1
                indexDict[cur_level] += 1
            else:
                indexDict[cur_level] += 1

        S1.popleft()

    return answer


print(solution("ppwwwbpbbwwbw", "pwbwpwwbw"))  # 640
print(solution("b", "w"))  # 1024
