bs = int(input("Enter the basic salary"))
HRA = 10 / 100 * bs
da = 73 / 100 * bs
gs = bs + da + HRA
IT = 30 / 100 * gs
ns = gs - IT
print("The net salary is = ", ns)

