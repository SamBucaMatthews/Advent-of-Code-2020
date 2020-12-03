import math

def count_trees(right_slope, down_slope):
    index = right_slope
    count = 0

    for row in rows[down_slope::down_slope]:
        while len(row) <= index:
            row = row + row

        if row[index] == "#":
            count = count + 1
        index = index + right_slope

    return count

with open("input.txt") as file:
    rows = file.read().splitlines()

cases = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

result = math.prod([count_trees(*i) for i in cases])
print(result)
