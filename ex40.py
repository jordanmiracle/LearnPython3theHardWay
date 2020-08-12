class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"


    def apple(self):
        print("I am classy apples!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)




# Each time you creating a variable and assign it to MyStuff, you are creating a new object.
# You are instantiating, or creating an instance.


# This is dict style

# mystuff['apples']

# This is module style (after import)

# mystuff.apples()
# print(mystuff.tangerine)

# this is class style

# thing = MyStuff()
# thing.apples()
# print(thing.tangerine)
