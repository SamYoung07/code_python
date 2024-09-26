start = float(input("Initial amount of money: "))
cookies = input("Cookies Sold: ")
cookie = list(cookies)
big = 0
small = 0
for i in cookie:
    if(i == "b"):
        big = big + 1
    else:
        small = small + 1
print(f"Number of cookies sold: {big+small}")
normal_cost = small*0.75
big_cost = big*1.25
print(f"Profit: {big_cost+normal_cost}")
print(f"Total Money: {start + big_cost + normal_cost}")