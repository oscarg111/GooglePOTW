# Opens the file
file = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\ATL_BELTLINE_STREETART.txt.txt", 'r')

# Reads the text file
f = file.readlines()

# Creates an array in which we will input the items in the text file and count variables
new_list = []
counta = 0
countA = 0

# for loop that adds the items in the text file to the array
for line in f:
    new_list.append(line[:-1])

# counts the 'a' and "a" in the array
for x in range(len(new_list)):
    for y in range(len(new_list[x]) - 2):
        new_list[x] = new_list[x].upper()
        if(new_list[x][y] == "A" and new_list[x][y + 1] == "T" and new_list[x][y + 2] == "L"): # if the character at position y of line x is "a" the counta variable increases
            counta += 1
    countA += new_list[x].count("ATLANTA")

# prints counta countA and the total
print(counta)
print(countA)
print(counta - countA)

# closes the file
file.close()