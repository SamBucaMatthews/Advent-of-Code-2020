def get_row_number(boarding_pass: str):
    bottom = 0
    top = 127

    for letter in boarding_pass[:7]:
        half = int((top + bottom ) / 2)

        if letter == "F":
            top = half
        elif letter == "B":
            bottom = half

    return min(bottom + 1, top + 1)

def get_column_number(boarding_pass: str):
    bottom = 0
    top = 7

    for letter in boarding_pass[7:]:
        half = int((top + bottom ) / 2)

        if letter == "L":
            top = half
        elif letter == "R":
            bottom = half
    
    return max(bottom, top)

def get_seat_id(boarding_pass: str):
    return get_row_number(boarding_pass) * 8 + get_column_number(boarding_pass)

def find_seat_id(rows):
    rows.sort()
    return [x for x in range(rows[0], rows[-1]+1) if x not in rows][0]
    

with open("input.txt") as input_file:
    inputs = input_file.read().splitlines()

rows = [get_seat_id(boarding_pass) for boarding_pass in inputs]

print(max(rows))
print(find_seat_id(rows))

print(get_seat_id("BFFFBBFRRR") == 567)
print(get_seat_id("FFFBBBFRRR") == 119)
print(get_seat_id("BBFFBBFRLL") == 820)