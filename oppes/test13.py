n = int(input())
li = []
for i in range(n):
    li.append(str(input()))

for words in li:
    ins = words.split(',')
    mx=[]
    for i in range(1, len(ins)):
        if ins[i][0] == ins[i - 1][-1]:
            if len(mx)==0:
                mx.append(ins[i])
            mx.append(ins[i])
        elif len(mx)!=0:
            break
    if len(mx)==0:
        print(1)
    else:
        print(len(mx))
