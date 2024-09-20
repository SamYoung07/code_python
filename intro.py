first = input("First Name: ")
last = input("Last Name: ")
birth = input("Birthyear: ")
age = 2024 - int(birth)
print(f"Hello {first} {last}")
print(f"You are {age} years old")
if age > 18:
    print("You are old enough to drink")
else: 
    print("You are not old enough to drink")