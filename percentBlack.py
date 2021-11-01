file = open("MATRIX.txt")
f = file.readlines()

# stores values of file into array
f_lines = []
for line in f:
    f_lines.append(line[:-1])

# counter variables
count_white = 0
count_black = 0

# counts black and white pixels
for x in range(len(f_lines)):
    for y in range(len(f_lines[x])):
        if f_lines[x][y] == '0':
            count_black += 1
        if f_lines[x][y] == '1':
            count_white += 1

# prints black pixels and white pixels
print(count_black)
print(count_white)

# finds the percentage of black and white pixels
print(count_black / (count_white + count_black))