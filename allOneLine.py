from urllib.request import urlretrieve

url = "https://google.qualtrics.com/CP/File.php?F=F_3pETar4WGgxSjoq"
# saves the url as file onto my computer
urlretrieve(url, 'MATRIX.txt')

# this program will test to see how many lines in MATRIX.txt are the same number
file = open("MATRIX.txt")
f = file.readlines()

# stores values of file into array
f_lines = []
for line in f:
    f_lines.append(line[:-1])

# counter variables
total_lines = len(f_lines)
print(total_lines)

# subtracts one from the total length if there are two different characters in the string
for x in range(len(f_lines)):
    if f_lines[x][0] == "1" and "0" in f_lines[x]:
        total_lines -= 1
    elif f_lines[x][0] == "0" and "1" in f_lines[x]:
            total_lines -= 1

# prints all oneliners
print(total_lines)