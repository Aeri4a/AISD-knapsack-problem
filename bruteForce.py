import itertools


def bruteForce(weights, values, capacity):
    max_val = 0
    n = len(weights)
    all_combinations = [[0, 1] for i in range(n)]

    for c in itertools.product(*all_combinations):
        val = 0
        w = 0
        for i in range(len(c)):
            if w > capacity:
                break

            val += c[i] * values[i]
            w += c[i] * weights[i]

        if w <= capacity and val > max_val:
            max_val = val

    return max_val
