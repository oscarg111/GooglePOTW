from urllib.request import urlretrieve

url = "https://google.qualtrics.com/CP/File.php?F=F_3pETar4WGgxSjoq"
# saves the url as file onto my computer
urlretrieve(url, 'MATRIX.txt')

file = open("MATRIX.txt")
f = file.readlines()

# stores values of URL into array
f_lines = []
for line in f:
    f_lines.append(line[:-1])

count_0 = 0

# iterates through array and adds one to count_0 if it is '0', which is black
for x in range(len(f_lines[299])):
    if f_lines[299][x] == '0':
        count_0 += 1

print(count_0)