from pprint import pprint

with open('2_input.txt') as f:
    rows = [list(map(int, row.split())) for row in f.readlines()]

total = 0

print(len([row for row in rows if sorted(row) == row or sorted(row, reverse=True) == row]))

for row in rows:
    
    safe = True
    if sorted(row) == row or sorted(row, reverse=True) == row:

        for i in range(1, len(row)):
            if not 1 <= abs(row[i-1] - row[i]) <= 3:
                safe = False
                break

        if safe:
            total += 1
print(total)
