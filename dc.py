import random
print("Enter the DC")
dc = int(input())
dice = random.randint(1,21)
print(f"You rolled a {dice}!")
if (dice >= dc):
    print("The task was successful")
else:
    print("The task was not successful")