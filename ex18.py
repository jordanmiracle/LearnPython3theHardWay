def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 {arg2}")


# okay, that *args was pointless, we can just do this instead
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


#  this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#  this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Jordan", "Miracle")
print_two_again("Jordan", "Miracle")
print_one("First!")
print_none()

