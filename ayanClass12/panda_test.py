import pandas as pd

li = []
for q in range(0, 73):
    li.append(q)
s = pd.Series(li)
print(s)
