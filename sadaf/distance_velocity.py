# WAP to input u (initial velocity) v (final velocity) and a(acceleraƟon) and t (Ɵme) and
# print displacement done. [Displacement =𝑢𝑡 + 0.5𝑎𝑡^2]

u = float(input("Enter the initial velocity "))
a = float(input("Enter the acceleration "))
t = float(input("Enter the time "))
d = u * t + 0.5 * a * t * t
print("The displacement is = ", d)
