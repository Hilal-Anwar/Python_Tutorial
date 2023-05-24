class Human:
    age = 0
    weight = 0
    gender = ''


class Person(Human):
    def __init__(self, age, weight, gender):
        self.age = age
        self.weight = weight
        self.gender = gender


print(Person(20, 35, "male").__annotations__)
