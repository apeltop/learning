from collections import defaultdict


def solution(edges):
    answer = []
    graph_8_count = 0
    graph_bar_count = 0
    graph_donut_count = 0

    def find_center_node():
        start_a_dict = defaultdict(int)
        m_k, m_v = 0, 0
        for edge in edges:
            start_a_dict[edge[0]] += 1
            if start_a_dict[edge[0]] > m_v:
                m_k = edge[0]
                m_v = start_a_dict[edge[0]]
            if m_v == 3:
                return m_k
        return m_k

    center_node = find_center_node()

    def remove_and_get_start_nodes_start_center_node():
        start_nodes = []
        for edge in edges:
            if edge[0] == center_node:
                start_nodes.append(edge[1])
        return start_nodes

    start_nodes = remove_and_get_start_nodes_start_center_node()

    edge_dict = defaultdict(list)
    for edge in edges:
        if edge[0] == center_node:
            continue

        edge_dict[edge[0]].append(edge[1])

    for start_node in start_nodes:
        groups = [start_node]
        is_graph_8 = False

        r = start_node

        while r in edge_dict:
            r_dest_nodes = edge_dict[r]

            if len(r_dest_nodes) > 1:
                is_graph_8 = True
                break

            r = r_dest_nodes[0]
            groups.append(r)

            if r == start_node:
                break

        if is_graph_8:
            graph_8_count += 1
        elif len(groups) == 1:
            graph_bar_count += 1
        elif groups[0] == groups[-1]:
            graph_donut_count += 1
        else:
            graph_bar_count += 1

    return [center_node, graph_donut_count, graph_bar_count, graph_8_count]


# print(solution([[i, i + 1] for i in range(0, 1000000, 1)]))
# print(solution([[i, i + 1] for i in range(0, 1000000, 1)]))
# print(solution([[i, i + 1] for i in range(0, 2000000, 2)]))

print((solution([[2, 3], [4, 3], [1, 1], [2, 1]])), [2, 1, 1, 0])

print((solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8]])), [4, 0, 1, 2])

print((solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8], [20, 20], [4, 20]])), [4, 1, 1, 2])
