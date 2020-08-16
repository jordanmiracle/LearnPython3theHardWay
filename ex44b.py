class Parent(object):

    def override(self):
        print("PARENT override()")

    def player(self, health, armor, damage):
        self.health = health
        self.armor = armor 
        self.damage = damage
        print (f" health is {health}. Armor is {armor}, and damage is {damage}.")

class Child(Parent):

    def override(self):
        print("CHILD override()")
        super(Child, self).player(70, 200, 80)
    


dad = Parent()
son = Child()

dad.override()
son.override()

dad.player(100, 150, 50)
son.player(70, 200, 80)