def backtracking(weights, values, capacity):
    if not weights or capacity <= 0:
        return 0

    if weights[0] <= capacity:
        return max(
            values[0] +
            backtracking(
                weights[1:], values[1:], capacity-weights[0]),
            backtracking(weights[1:], values[1:], capacity))
    else:
        return backtracking(weights[1:], values[1:], capacity)
