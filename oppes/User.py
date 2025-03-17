class User:
    name = ""
    age = 0
    gender = ""
    userid = ""

    def __init__(self, name, age, gender, userid):
        self.name = name
        self.gender = gender
        self.age = age
        self.userid = userid

    def find_max(self, a):
        mx = a[0]
        mi = a[0]
        for i in a:
            mx = max(i, mx)
            mi = min(i, mi)
        return mx, mi


if __name__ == "__main__":
    user = User("hilal", 26, "male", "762323")
    ar = [5, 6, 5, 4, -4, 45, 454]
    print(user.find_max(ar))
