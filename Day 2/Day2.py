with open("input.txt") as input_file:
    input = input_file.read().splitlines()

def is_valid(value):
    parts = value.split(": ")
    password = parts[1]
    search_letter = parts[0].split()[1]
    search_range = parts[0].split()[0]
    min = int(search_range.split("-")[0])
    max = int(search_range.split("-")[1])

    count = password.count(search_letter)

    return count >= min and count <= max

results = [is_valid(i) for i in input]

print(results.count(True))