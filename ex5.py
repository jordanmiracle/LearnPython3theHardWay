name = 'Jordan M Miracle'
age = 29
height = 75 # inches
weight = 155 #  lbs
eyes = 'Blue'
hair = 'Brown'
teeth = 'Whitish'

new_height = height * 2.54
new_weight = weight * .454

print(f"Let's talk about {name}.")
print(f"He's {new_height} cm tall.")
print(f"He's {new_weight} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total =  age +  height +  weight
print(f"If I add {age}, {new_height}, and {new_weight} I get {total}.")