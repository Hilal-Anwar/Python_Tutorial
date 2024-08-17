# how to make a list

athar = [5, 12, 15, 97, -8, 5, 4, 9, "apple"]
ali = []
print(athar[0])
print(athar[3])
print(athar[7])
# print(athar[8])
athar.append(48)
print(athar)
print(athar.__len__())

# how to fill list by user

ali.append(int(input("Enter a number \n")))
ali.append(int(input("Enter a number \n")))
ali.append(int(input("Enter a number \n")))
ali.append(int(input("Enter a number \n")))
ali.append(int(input("Enter a number \n")))
print(ali)

helal = []
for i in range(0, 10):
    n = int(input("Enter the "+str(i+1)+" number \n"))
    helal.append(n)
