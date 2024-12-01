with open('1_input.txt') as f:
    rows = [list(map(int, row.split())) for row in f.readlines()]

left, right = zip(*rows)
total = sum([l * right.count(l) for l in left])
print(total)
