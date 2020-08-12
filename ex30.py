people = 1
cars = 1
trucks = 10
#  Checks to see if cars are greater than people
if cars > people:
    print("We should take the cars.")
#  If cars are not greater than people, checks to see if cars are less than people.
elif cars < people:
    print("We should not take the cars.")
#  This is saying, if they are not greater or less, than print we cannot decide
else:
    print("We can't decide.")
#  Checks to see if trucks are greater than cars
if trucks > cars:
    print("That's too many trucks.")
#  If above is False then checks to see if trucks are less than cars
elif trucks < cars:
    print("Maybe we should take the trucks.")
#  Otherwise, print we cannot decide
else:
    print("We still can't decide.")
#  Checks to see if people are greater than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
    #  Otherwise, prints let's stay home
else:
    print("Fine, let's stay home then.")