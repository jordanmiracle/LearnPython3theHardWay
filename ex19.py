def cheese_and_crackers(cheese_count, boxes_of_crackers):   # This defines a function called cheese and crackers and gives it two arguments
    print(f"You have {cheese_count} cheeses!")  #  prints a formatted str that uses the cheese count argument
    print(f"You have {boxes_of_crackers} boxes of crackers!")   #  prints a formatted str that uses the boxes of crackers argument
    print("Man that's enough for a party!")    # prints another line
    print("Get a blanket.\n")   # prints get a blanket

print("We can just give the function numbers directly:")    # prints a str saying that we can give the function numbers directly
cheese_and_crackers(20, 30)    #  calls cheese_and_crackers and gives 20 and 30 as arguments, respectively

print("OR, we can use variables from our script:")  #  or, we can take variables that we may have...
amount_of_cheese = 10   #  in our script/program, and use those as function arguments
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)   #  Call the cheese_and_crackers function, 
                                                            #  and use the two variables from lines 11 and 12 as arguments.
print("We can even do math inside too:")    #  More printing and explaining
cheese_and_crackers(10 + 20, 5 + 6)    #  calling cheese_and_crackers and then using two arithmetic expressions as the arguments

print("And we can combine the two, variables and math:")    # printing
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)    #  calls cheese_and_crackers, and gives the two variables created above, 
                                                                            #  plus an integer as arguments. You can get quite creative this way.
