from sys import argv    #  imports argv from sys

script, filename = argv    #  sets variables to argv

print(f"We're going to erase {filename}.")  #  prints the filename that is to be erased
print("If you don't want that hit CRTL-C (^C).")   #  Gives an option to cancel
print("If you do want that, hit return.")   #  the option to enter and proceed

input("?")  #  asks for input

print("Opening the file...")    #  prints opening the file
target = open(filename, 'w')    #  sets opening the file in write mode to a variable

print("Truncating the file. Goodbye!")  #  prints that the file is truncating
target.truncate()   #  calls the truncate function on the target file

print("Now I'm going to ask you for three lines.")  #  prints again 

line1 = input("line 1: ")    #  gives 3 lines to add text to the new file
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")  #  says we are going to print these

target.write(f"""{line1} \n {line2} \n {line3} \n""")    #  uses the write function on the next 3 lines, with newlines in between


print("And finally, we close it.")
target.close()  #  closes the file