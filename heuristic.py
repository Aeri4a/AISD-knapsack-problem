def heuristicDO(W, arr, choice):
    if choice == 2:
        arr.sort(key=lambda x: x[1])
    if choice == 3:
        arr.sort(key=lambda x: x[0], reverse=True)
    if choice == 4:
        arr.sort(key=lambda x: (x[0]/x[1]), reverse=True)

    finalvalue = 0

    for item in arr:
        if item[1] <= W:
            W -= item[1]
            finalvalue += item[0]

    return finalvalue


def heuristic(size, value, b, choice):
    array = [(value[i], size[i]) for i in range(len(size))]

    return heuristicDO(b, array, choice)
