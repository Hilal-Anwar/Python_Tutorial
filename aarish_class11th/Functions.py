def message():
    print("Message from a function")
    print("I am not main function")
    print("But i was called from main function")


def message2():
    print("I am inside message 2")


if __name__ == "__main__":
    message()
    message2()
