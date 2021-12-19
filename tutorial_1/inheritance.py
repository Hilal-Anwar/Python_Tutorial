class human:
    a=0
    b=0
    c=""


class man(human):
    def __init__(self,age,weight):
        self.a=age
        self.b=weight
        self.c="male"
print(man(20,35).b)
