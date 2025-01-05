# nested loop
"""
    *
   * *
  * * *
 * * * *
* * * * *

1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1

"""
size = 5
k = size
for i in range(1, size + 1):
    for k in range(1, k + 1):
        print(" ", end='')
    for j in range(1, i + 1):
        print('* ', end='')
    k = k - 1
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if j % 2 == 0:
            print(0, "", end='')
        else:
            print(1, "", end='')
    print()
