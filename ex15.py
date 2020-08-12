#  importd sys from argv
from sys import argv
#  use argv to get a filename, just assign two variables to arg v that you can replace with the name 
# of the script and a filename later.
script, filename = argv    #  Lines 1-3 use argv to get a filename.
# set opening the filename to a variable, in this case txt.
txt = open(filename)
# this prints the name of the file you input
input(f"Here's your file {filename}:")
#  this prints the txt that is in the file you input
print(txt.read())
txt.close()

#  this asks for another file
print("Type the filename again:")
# this is the prompt
file_again = input("> ")
#  this opens another file and reads it
txt_again = open(file_again)
#  this prints it out
print(txt_again.read())
txt_again.close()

