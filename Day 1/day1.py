import math
import itertools

def product_of_combinations(count_of_entries):
    for combination in itertools.combinations(values, count_of_entries):
        if sum(combination) == 2020:
            result = math.prod(combination)
            return result


with open("day-1-input.txt") as input_file:
    values = [int(l) for l in input_file.read().splitlines()]

print(product_of_combinations(2))
print(product_of_combinations(3))