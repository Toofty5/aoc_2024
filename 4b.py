with open('4_input.txt', 'r') as f:
    matrix = [line.strip() for line in f.readlines()]
print(matrix)

total = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):

        # check above
        if row >= 3:
            #UL
            if col >= 3:
                check = ''
                for x in range(4):
                    check += matrix[row-x][col-x]
                if check == "XMAS":
                    print("UL")
                    total += 1
            #up
            check = ''
            for x in range(4):
                check += matrix[row-x][col]
            if check == "XMAS":
                total += 1
                print('UP')

            #UR
            if col <= len(matrix[0]) - 4:
                check = ''
                for x in range(4):
                    check += matrix[row-x][col+x]
                if check == "XMAS":
                    total += 1
                    print("UR")


        # check below
        if row < len(matrix) - 3:
            #DL
            if col >= 3:
                check = ''
                for x in range(4):
                    check += matrix[row+x][col-x]
                if check == "XMAS":
                    total += 1
                    print("DL")
            #down
            check = ''
            for x in range(4):
                check += matrix[row+x][col]
            if check == "XMAS":
                total += 1
                print("DOWN")

            #DR
            if col <= len(matrix[0]) - 4:
                check = ''
                for x in range(4):
                    check += matrix[row+x][col+x]
                if check == "XMAS":
                    total += 1
                    print("DR")
        
        # check sides
        if col >= 3 and matrix[row][col-3:col+1] == "SAMX":
            total += 1
            print("left")

        if col < len(matrix[0]) and matrix[row][col:col+4] == "XMAS":
            total += 1
            print("right")


print(total)
