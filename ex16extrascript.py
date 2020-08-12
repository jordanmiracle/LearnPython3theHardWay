from sys import argv

script, filename = argv

print("Do you want to read this file?")
input("Press enter to proceed and ctrl-c to exit.")

print("Opening the file...")
target = open(filename, 'r')

file = target.read()
print(file)

prompt = input("> ")
file.write(prompt)

print("And now we close it.")
target.close()
