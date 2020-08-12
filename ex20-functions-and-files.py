from sys import argv    #  imports argv

script, input_file = argv   #  sets variables

def print_all(f):   #  defines a function that calls read on a file 
    print(f.read())


def rewind(f):  #  defines a function that seeks or rewinds to a certain point in the file. This is in bytes, not characters
    f.seek(0)


def print_a_line(line_count, f):    #  This finds each /n character and the stops reading the file to return what it has found so far
    print(line_count, f.readline())


current_file = open(input_file, 'r') # This opens whatever file we add as an argument for input_file when we run the code

print("First let's print the whole file:\n") 
#  Prints the whole file
print_all(current_file) # This call print_all, which reads the file, on current_file, which we have set to open our argument.

print("Now let's rewind, kind of like a tape.")

rewind(current_file)    #  This calls seek on our file, which moves the file to the first byte.

print("Let's print 3 lines:")

current_line = 1    #  calls readline on first line 
print_a_line(current_line, current_file)

current_line = current_line + 1    # calls readline on next line
print(current_line, current_file)

current_line = current_line + 1
print(current_line, current_file)   #  calls readline on 3rd line
