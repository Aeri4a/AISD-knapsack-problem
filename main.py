import random
import time
from excelExport import *
from dynamic import *
from bruteForce import *
from backtracking import *
from heuristic import *

# # Generate
# n = 30
# size = [random.randint(10, 1000) for i in range(n)]
# value = [random.randint(100, 10000) for i in range(n)]
# b = sum(size) // 2

# -= TASK 1 =-
# --- GENERATE RANGES --
n = 10
startNumber = 4
step = 2
dataRange = [x for x in range(
    startNumber, startNumber + (n - 1) * step + 1, step)]

# --- TEMPLATES ---
tempTask1 = [{
    "name": "packages nr",
    "data": [*dataRange]
},
    {
    "name": "PD",
    "data": []
},
    {
    "name": "BF1",
    "data": []
},
    {
    "name": "BF2",
    "data": []
},
    {
    "name": "GH4",
    "data": []
}
]

# --- GENERATE DATA ---
for r in dataRange:
    size = [random.randint(10, 1000) for i in range(r)]
    value = [random.randint(100, 10000) for i in range(r)]
    b = sum(size) // 2

    # - Dynamic Programming PD -
    startDynamic = time.time_ns()
    dynamic(b, size, value, r)
    resultDynamic = time.time_ns() - startDynamic

    # - Brute Force 1 BF1 -
    startBrute = time.time_ns()
    bruteForce(size, value, b)
    resultBrute = time.time_ns() - startBrute

    # - Brute Force 2 (Backtracking) BF2 -
    startBacktracking = time.time_ns()
    backtracking(size, value, b)
    resultBacktracking = time.time_ns() - startBacktracking

    # - Heuristic 4 [value/size] GH4 -
    startHeuristic4 = time.time_ns()
    heuristic(size, value, b, 4)
    resultHeuristic4 = time.time_ns() - startHeuristic4

    # --- Insert collected data to template ---
    # - 4 algorithms -
    tempTask1[1]["data"].append(resultDynamic)
    tempTask1[2]["data"].append(resultBrute)
    tempTask1[3]["data"].append(resultBacktracking)
    tempTask1[4]["data"].append(resultHeuristic4)


# -= TASK 2 =-
# --- GENERATE RANGES --
n = 10
startNumber = 4
step = 2
dataRange = [
    x for x in range(startNumber, startNumber + (n - 1) * step + 1, step)
]

# --- TEMPLATES ---
tempTask2 = [{
    "name": "packages nr",
    "data": [*dataRange]
},
    {
    "name": "PD-b25",
    "data": []
},
    {
    "name": "PD-b75",
    "data": []
},
    {
    "name": "BF1-b25",
    "data": []
},
    {
    "name": "BF1-b75",
    "data": []
},
    {
    "name": "BF2-b25",
    "data": []
},
    {
    "name": "BF2-b75",
    "data": []
},
    {
    "name": "GH4-d25",
    "data": []
},
    {
    "name": "GH4-d75",
    "data": []
}]

# --- GENERATE DATA ---
bRange = [0.25, 0.75]

for br in bRange:
    i = 1
    for r in dataRange:
        size = [random.randint(10, 1000) for i in range(r)]
        value = [random.randint(100, 10000) for i in range(r)]
        b = int(sum(size) * br)

        # - Dynamic Programming [PD] -
        startDynamic = time.time_ns()
        dynamic(b, size, value, r)
        endDynamic = time.time_ns() - startDynamic

        # - Brute Force [BF1] -
        startBrute = time.time_ns()
        bruteForce(size, value, b)
        endBrute = time.time_ns() - startBrute

        # - Backtracking [BF2] -
        startBacktracking = time.time_ns()
        backtracking(size, value, b)
        endBacktracking = time.time_ns() - startBacktracking

        # - Heuristic 4 [GH4] -
        startHeuristic4 = time.time_ns()
        heuristic(size, value, b, 4)
        endHeuristic4 = time.time_ns() - startHeuristic4

        # - Add to templates -
        tempTask2[i]["data"].append(endDynamic)
        tempTask2[i+2]["data"].append(endBrute)
        tempTask2[i+4]["data"].append(endBacktracking)
        tempTask2[i+6]["data"].append(endHeuristic4)

    i += 1

# -= TASK 3 =-
# --- GENERATE RANGES ---
n = 10
startNumber = 4
step = 2
dataRange = [
    x for x in range(startNumber, startNumber + (n - 1) * step + 1, step)
]

# --- TEMPLATES ---
bRange = [0.25, 0.50, 0.75]

# tempTask3_25, tempTask3_5, tempTask3_75
for b in bRange:
    B = str(b)[2:]
    globals()[f'tempTask3_{B}'] = [{
        "name": "packages nr",
        "data": [*dataRange]
    },
        {
        "name": "PD",
        "data": []
    },
        {
        "name": "GH1",
        "data": []
    },
        {
        "name": "GH2",
        "data": []
    },
        {
        "name": "GH3",
        "data": []
    },
        {
        "name": "GH4",
        "data": []
    }
    ]

# --- GENERATE DATA ---
for br in bRange:
    for r in dataRange:
        size = [random.randint(10, 1000) for i in range(r)]
        value = [random.randint(100, 10000) for i in range(r)]
        b = int(sum(size) * br)

        # - PD -
        resPD = dynamic(b, size, value, r)
        # - GH1 -
        resGH1 = heuristic(size, value, b, 1)
        avgDevGH1 = (resPD-resGH1)/resPD * 100
        # - GH2 -
        resGH2 = heuristic(size, value, b, 2)
        avgDevGH2 = (resPD-resGH2)/resPD * 100
        # - GH3 -
        resGH3 = heuristic(size, value, b, 3)
        avgDevGH3 = (resPD-resGH3)/resPD * 100
        # - GH4 -
        resGH4 = heuristic(size, value, b, 4)
        avgDevGH4 = (resPD-resGH4)/resPD * 100

        # - Add to templates -
        B = str(br)[2:]
        globals()[f'tempTask3_{B}'][1]["data"].append(resPD)
        globals()[f'tempTask3_{B}'][2]["data"].append(avgDevGH1)
        globals()[f'tempTask3_{B}'][3]["data"].append(avgDevGH2)
        globals()[f'tempTask3_{B}'][4]["data"].append(avgDevGH3)
        globals()[f'tempTask3_{B}'][5]["data"].append(avgDevGH4)


# - EXCEL -
# Task 1
excelExport("results-excel", "task1", tempTask1)
# Task 2
excelExport("results-excel", "task2", tempTask2)
# Task 3
excelExport("results-excel", "task3-b25", tempTask3_25)
excelExport("results-excel", "task3-b50", tempTask3_5)
excelExport("results-excel", "task3-b75", tempTask3_75)
