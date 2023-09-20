class Animal:
    def __init__(self, movement, food):
        self.movement = movement
        self.food = food

class Dog(Animal):
    name = ""
    def __init__(self, id, movement, food):
        self.id = id
        Animal.__init__(self, movement, food)
    def print_id(self):
        print(self.id)

class Bird(Animal):
    def __init__(self, food):
        Animal.__init__(self, "flying", food)


class Seagull(Bird):
    def scream(self):
        print("*seagulls screaming in the distance*")
