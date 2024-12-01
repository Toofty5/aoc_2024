from pprint import pprint

with open('1_input.txt') as f:
    rows = [list(map(int, row.split())) for row in f.readlines()]

sorted_rows = [*zip(sorted([l for l, r in rows]) ,sorted([r for l,r in rows]))]
print(sum([abs(a-b) for a,b in sorted_rows]))
