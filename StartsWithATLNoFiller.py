# opens both files
file = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\movies.txt", 'r')
file2 = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\movies_short_list.txt", 'r')

# reads the lines in both of the files
f = file.readlines()
f2 = file2.readlines()

# creates arrays that store the values in the files and count variables
f_lines = []
f2_lines = []
z = 0
countA = 0
countT = 0
countL = 0

# defines a function which stores the lines of a file into an array
def inFile(file_obj, new_line = []):
    for line in file_obj:
        new_line.append(line[:-1])

# defines a function which counts the movies starting with "A", "T", or "L"
def countATL(new_line = [], count_A = 0, count_T = 0, count_L = 0, zz = 0):
    for x in range(len(new_line)):
        if new_line[x].startswith('The '):
            if new_line[x][4] is 'A':
                count_A += 1
            if new_line[x][4] is 'T':
                count_T += 1
            if new_line[x][4] is 'L':
                count_L += 1
        elif new_line[x].startswith('A '):
            if new_line[x][2] is 'A':
                count_A += 1
            if new_line[x][2] is 'T':
                count_T += 1
            if new_line[x][2] is 'L':
                count_L += 1
        elif new_line[x].startswith('An '):
            if new_line[x][3] is 'A':
                count_A += 1
            if new_line[x][3] is 'T':
                count_T += 1
            if new_line[x][3] is 'L':
                count_L += 1
        else:
            if new_line[x][0] is 'A':
                count_A += 1
            if new_line[x][0] is 'T':
                count_T += 1
            if new_line[x][0] is 'L':
                count_L += 1

    return (count_A + count_T + count_L + zz)

# calls the functions
inFile(f, f_lines)
inFile(f2, f2_lines)
print(z)
print(countATL(f_lines, countA, countT, countL, z))
print(countATL(f2_lines, countA, countT, countL, z))
print(countATL(f2_lines, countA, countT, countL, z) + countATL(f_lines, countA, countT, countL, z))
print(z)
