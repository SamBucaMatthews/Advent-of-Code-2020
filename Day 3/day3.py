import math

# Example given should be 7
# rows = [
#     "..##.......",
#     "#...#...#..",
#     ".#....#..#.",
#     "..#.#...#.#",
#     ".#...##..#.",
#     "..#.##.....",
#     ".#.#.#....#",
#     ".#........#",
#     "#.##...#...",
#     "#...##....#",
#     ".#..#...#.#",
#     ]


with open(r"D:\Code\Advent of Code 2020\Day 3\input.txt") as file:
    rows = file.read().splitlines()

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

cases = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

for case in cases:
    print(count_trees(*case))

result = math.prod([count_trees(*i) for i in cases])
print(result)
