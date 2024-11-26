def solution(data, ext, val_ext, sort_by):
    answer = [[]]

    # code	date	maximum	remain
    datas = []
    d_index = 0
    if ext == "date":
        d_index = 1
    if ext == "maximum":
        d_index = 2
    if ext == "remain":
        d_index = 3

    s_index = 0
    if sort_by == "date":
        s_index = 1
    if sort_by == "maximum":
        s_index = 2
    if sort_by == "remain":
        s_index = 3

    for d in data:
        if val_ext > d[d_index]:
            datas.append(d)

    datas.sort(key=lambda x: x[s_index])

    return datas


print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"),
      [[3, 20300401, 10, 8], [1, 20300104, 100, 80]])
