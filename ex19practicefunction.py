from datetime import datetime

def hours_per_day(sleep, awake):
    hours_of_sleep = int(input("Enter your hours of sleep."))
    awake = 24 - hours_of_sleep
    print(f"You are getting {hours_of_sleep} hours of sleep.")
    print(f"Which means you are awake {awake} hours of the day.\n")

print("This is just passing numbers in directly.")
hours_per_day(8, 16)

print("This is using variables that we created.")
hours_asleep = 8
hours_awake = 16

hours_per_day(hours_asleep, hours_awake)

print("This is one way to do math inside of a function, while mixing variables in.")
hours_per_day(hours_asleep - 1, hours_awake + 1)






