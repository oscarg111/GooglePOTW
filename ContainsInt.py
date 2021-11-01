print("Running ContainsInt")
# opens both files
file = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\movies.txt", 'r')
file2 = open("C:\\Users\\oscar\\OneDrive\\Desktop\\Google Problem of the Week\\movies_short_list.txt", 'r')

# reads the lines in both of the files
f = file.readlines()
f2 = file2.readlines()

# creates arrays that store the values in the files and count variables
# and a counter
f_lines = []
f2_lines = []
int_counter = 0

# defines a function which stores the lines of a file into an array
def inFile(file_obj, new_line = []):

    for line in file_obj:

        new_line.append(line[:-1])

# calls function
inFile(f, f_lines)
inFile(f2, f2_lines)

# defines a function that finds the index of the first digit and tests to see if it is
# before the start of the date in the movie title
def containsInt(array = [], intCounter = 0):

    for x in range(len(array)):

        for i, c in enumerate(array[x]):

            if c.isdigit():
                break

        if i < len(array[x]) - 6:

            intCounter += 1

    return intCounter

# calls the function
print(containsInt(f_lines, int_counter))
print(containsInt(f2_lines, int_counter))
