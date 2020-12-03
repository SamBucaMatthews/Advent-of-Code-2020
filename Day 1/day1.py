import os
import itertools

with open("day-1-input.txt") as input_file:
    values = [int(l) for l in input_file.read().splitlines()] 

for combination in itertools.combinations(values, 2):
    if combination[0] + combination[1] == 2020:
        result = combination[0] * combination[1]
        print(result)
