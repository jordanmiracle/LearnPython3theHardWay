## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    def __init__(self, name):
        self.name = name


## Dog is-a Animal
class Dog(Animal):
    genus = 'canis'

    def __init__(self, name):
        ## Dog has-a attribute named name
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)



## Cat is-a Animal
class Cat(Animal):
    family = 'felidae'
    genus = 'felis'
    def __init__(self, name):
        ## Cat has-a attribute name
        self.name = name

    def speak(self, utterance):
        return speak('mrow')


    def __str__(self, utternace):
        return f"{self.name} says {self.speak} when s/he wants food or scratches, or wants to talk."


class DomesticatedCat(Cat):
    def __init__(self, name):
        self.name = name
        self.genus = 'felis catus'



## Person is-a object (not really. You could use animal here too)
class Person(object):
    def __init__(self, name):
        ## Person has-a name of some kind
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm, what is this strange magic
        super(Employee, self).__init__(name)
        ## Employee has-a attribute salary
        self.salary = salary


    def clock_in(self, time):
        pass

## Fish is-a object
class Fish(Animal):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a employee with a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish('jordan')

## crouse is-a salmon
crouse = Salmon('Benedict')

## harry is-a halibut
harry = Halibut('humphrey')

