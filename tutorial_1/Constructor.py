import tutorial_1.make


class Constructor:
    def __init__(self, realpart, imagpart):
        self.x = realpart
        self.y = imagpart

    def fun(self):
        print(self.x + self.y)
        tutorial_1.make.hell.candey = "Beats"
        print(tutorial_1.make.hell.candey)


if __name__ == '__main__':
    c = Constructor(3.0, -4.5)
    print("(", c.x, ",", c.y, ")")
    c.fun()
