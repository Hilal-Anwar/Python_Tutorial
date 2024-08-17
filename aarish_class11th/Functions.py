def message():
    print("Message from a function")
    print("I am not main function")
    print("But i was called from main function")


def message2():
    print("I am inside message 2")


def even(a):
    if a % 2 == 0:
        print("Even number")
    else:
        print("Not a even number or it is odd")


def sum(a, b):
    s = a + b
    return s


if __name__ == "__main__":
    message()
    message2()
    even(27)
    su=sum(5, 6)
    print(su)
