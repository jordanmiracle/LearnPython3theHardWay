from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)   # open the file to copy from  
indata = in_file.read() #  read the original file
input("> ") #  ask for input

out_file = open(to_file, 'w')   #  opening the file that is to be written to
out_file.write(indata)  #  writing the data from the original file to the copy


out_file.close()        #  closes both files    
in_file.close()     #  closes both files

