with open('4_input.txt', 'r') as f:
    matrix = [line.strip() for line in f.readlines()]
print(matrix)

total = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'A' and 0 < row < len(matrix) - 1 and 0 < col < len(matrix[0]) - 1:
            uldr = matrix[row-1][col-1] + "A" + matrix[row+1][col+1]
            dlur = matrix[row+1][col-1] + "A" + matrix[row-1][col+1]
            if uldr in ['MAS', 'SAM'] and dlur in ['MAS', 'SAM']:
                total += 1

print(total)
