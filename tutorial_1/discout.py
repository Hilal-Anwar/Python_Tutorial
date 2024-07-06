mp = int(input("Enter the mp :"))
if mp <= 30000:
    amt = (1 - 5 / 100.0) * mp
if mp >= 30001 and mp <= 40001:
    amt = (1 - 10 / 100.0) * mp
if mp >= 40001 and mp <= 55000:
    amt = (1 - 12.5 / 100.0) * mp
if mp > 55000:
    amt = (1 - 15 / 100.0) * mp
print(amt)