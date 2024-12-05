from pprint import pprint
from copy import deepcopy

with open('2_input.txt') as f:
    rows = [list(map(int, row.split())) for row in f.readlines()]


def check_ascending(row, buffered):
    this_val = row[0]

    row_copy_a = deepcopy(row)
    row_copy_b = deepcopy(row)
    for i, val in enumerate(row[1:]):
        if not 1 <= val - this_val <= 3:
            if not buffered:
                print('buffering for ascend', row, val)
                row_copy_a.pop(i+1)
                row_copy_b.pop(i)
                return check_ascending(row_copy_a, True) or check_ascending(row_copy_b, True)
            else:
                print('rejecting ascend', row, 'delta', val - this_val)
                return False
        this_val = val
    return True


def check_descending(row, buffered):
    row_copy_a = deepcopy(row)
    row_copy_b = deepcopy(row)
    this_val = row[0]
    for i, val in enumerate(row[1:]):
        if not 1 <= this_val - val <= 3:
            if not buffered:
                print('buffering for descend', row, val)
                row_copy_a.pop(i+1)
                row_copy_b.pop(i)
                return check_descending(row_copy_a, True) or check_descending(row_copy_b, True)
            else:
                print('rejecting descend', row, 'delta', this_val - val)
                return False
        this_val = val
    return True

total = 0
for row in rows:
    if check_ascending(row, False) or check_descending(row, False):
        total += 1
        print(total)



print(total)


