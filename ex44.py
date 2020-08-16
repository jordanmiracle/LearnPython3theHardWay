class Parent(object):

    def override(self):   
        print(">>>Parent override, self")  # Creates a function, 'override' for the Parent class 
        print("PARENT override()")  # That prints PARENT override().
    
    def implicit(self):     # Creates a function named implicit
        print("PARENT implicit()")  # Prints "Parent implicit()"

    def altered(self):   # Creates function 'altered' that only takes self as an argument.
        print("PARENT altered()")  # Prints PARENT altered()


class Child(Parent):  #  Creates a subclass of parent, Child.
    
    def override(self):  # Creates a function, 'override' that DOES override the version of override in Parent
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

class
