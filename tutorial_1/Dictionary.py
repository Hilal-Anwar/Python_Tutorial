def tabularForm(a):
    print('{}     {}     {}'.format("Country name", "Country capital", "Currency"))
    for k, v in a.items():
        print('{}     {}     {}'.format(v[0], v[1], k))


if __name__ == '__main__':
    n = int(input("Enter the number of country \n"))
    a = dict();
    i = 0
    for i in range(n):
        name = str(input("Enter the name of country :\n"))
        capital = str(input("Enter its capital :\n"))
        currency = str(input("Enter the name of currency :\n"))
        a[currency] = [name, capital]
tabularForm(a)
key = str(input("Enter the name of currency for serching :\n"))
if (a.__contains__(key)):
    print("Name and the capital of the country with this currency", a[key])
else:
    print("No such currency is there")
