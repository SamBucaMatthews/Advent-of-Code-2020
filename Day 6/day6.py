def part_one(values):
    return sum([len(set("".join(value))) for value in values])

def part_two(group):
    v = set(group[0])
    for i in group[1:]:
        v = v.intersection(i)
    
    return len(v)

with open("input.txt") as input_file:
    values = [p.split() for p in input_file.read().split("\n\n")]


print(part_one(values))
print(sum([part_two(i) for i in values]))