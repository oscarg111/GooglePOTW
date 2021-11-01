print("Running 1990sMinus1980s.py")
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

#function variables
count80s = 0
count90s = 0

# defines a function that counts the amount of movies made in the 80s and 90s and subtracts them
def difference90s80s(lines = [], count_80s = 0, count_90s = 0):
    str = ""
    convertStr = ""
    for x in range(len(lines)):
        if lines[x][len(lines[x]) - 4] == "9":
            count_90s += 1
        if lines[x][len(lines[x]) - 4] == "8":
            count_80s += 1
        # for y in range(len(lines[x]) - 5, len(lines[x]) - 1):
        #         str += lines[x][y]
        # if str[len(str) - 2] == "8":
        #     count_80s += 1
        # if str[len(str) - 2] == "9":
        #     count_90s += 1
        # if str == "(199":
        #     count_90s += 1
        # if str == "(198":
        #     count_80s += 1
        # if str != "(195" and str != "(199":
        #     convertStr = float(str)
        #     if convertStr > 1979 and convertStr < 1990:
        #         count_80s +=1
        #     elif convertStr > 1989 and convertStr < 2000:
        #         count_90s +=1
            str = ""
            convertStr = ""
    return count_90s - count80s

movies = difference90s80s(f_lines, count80s, count90s)
shortMovies = difference90s80s(f2_lines, count80s, count90s)
print(movies)
print(shortMovies)
print(movies + shortMovies)
