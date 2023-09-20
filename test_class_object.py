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


class Seagull(Animal):
    def __init__(self, movement, food):
        Animal.__init__(self, movement, food)
    def scream(self):
        print("*seagull screaming in the distance*")


dog_list = []
new_seagull = Seagull("flying", "fish")

for i in range(0, 10):
    dog_list.append(Dog(i, "walking", "bones"))
for i in dog_list:
    i.print_id()

dog_list[0].name = "Tata"
print(dog_list[0].name)
new_seagull.scream()
