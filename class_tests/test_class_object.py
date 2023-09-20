from class_tests.test_class_file import *


def init_dog_list():
    dog_list = []
    for i in range(0, 10):
        dog_list.append(Dog(i, "walking", "bones"))
    dog_list[0].name = "Tata"
    return dog_list


def use_obj():
    dog_list = init_dog_list()
    seagull_1 = Seagull("fish")

    for i in dog_list:
        i.print_id()
    print(dog_list[0].name)
    seagull_1.scream()
    print("Seagulls eat {}".format(seagull_1.food))


if __name__ == "__main__":
    use_obj()
