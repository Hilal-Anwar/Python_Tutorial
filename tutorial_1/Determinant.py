def co_Factors(Matrix):
    dum1 = []
    dum2 = []
    dum3 = []
    for m in range(0, Matrix.__len__()):
        list1 = Matrix.__getitem__(m)
        for r in range(0, list1.__len__()):
            for i in range(1, list1.__getitem__(0).__len__()):
                for k in range(0, list1.__getitem__(0).__len__()):
                    if (r != k) & (list1.__getitem__(0).__getitem__(r) != 0.0):
                        if i == 1:
                            dum3.append(
                                pow(-1, r) * list1.__getitem__(0).__getitem__(r) * list1.__getitem__(i).__getitem__(k))
                        else:
                            dum3.append(list1.__getitem__(i).__getitem__(k))
                if dum3.__len__() != 0:
                    dum2.append(dum3)
                dum3 = []
            if dum2.__len__() != 0:
                dum1.append(dum2)
            dum2 = []
    return dum1


if __name__ == '__main__':
    determinant = []
    mem1 = []
    mem2 = []
    sum = 0.0
    size = int(input("Enter the size of square matrix \n"))
    for i in range(0, size):
        for j in range(0, size):
            # val = input("Enter the element for " + str((i + 1)) + " row " + " and " + str((j + 1)) + " column \n")
            mem1.append(float(1))
        mem2.append(mem1)
        mem1 = []
    determinant.append(mem2)
    print(determinant)
    for i in range(1, size - 1):
        determinant = co_Factors(determinant)
    print(determinant)
    for j in range(0, determinant.__len__()):
        lis = determinant.__getitem__(j)
        sum = sum + ((lis.__getitem__(0).__getitem__(0) * lis.__getitem__(1).__getitem__(1)) - (
                lis.__getitem__(0).__getitem__(1) * lis.__getitem__(1).__getitem__(0)))
    print(sum)
