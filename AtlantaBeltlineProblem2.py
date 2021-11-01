# Opens the file
file = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\ATL_BELTLINE_STREETART.txt.txt", 'r')

# Reads the text file
f = file.readlines()

# Creates an array in which we will input the items in the text file and count variables
new_list = []
line = ""


# for loop that adds the items in the text file to the array
for line in f:
    new_list.append(line[:-1])

for x in range(len(new_list)):
    line += new_list[x]

print(line[400])
print(line[500])
print(line[600])
print(line[700])
print(line[800])
print(line[900])
# closes the file
file.close()