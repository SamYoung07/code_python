import math
f1 = len(input("Enter the first fence: "))
f2 = len(input("Enter the second fence: "))
f3 = len(input("Enter the third fence: "))

total = f1 + f2 + f3
boxes = math.ceil(total/12)
leftover = (boxes*12)%total
cost = math.ceil(total/12) * 14.95

print(total)
print(leftover)
print(cost)