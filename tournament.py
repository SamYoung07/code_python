wins = 0
for i in range(6):
    result = input(f"Game {i+1} result: ")
    if (result == "W"):
        wins = wins + 1
if (wins == 0):
    print("Eliminated")
elif(wins < 3):
    print("Group 3")
elif(wins < 5):
    print("Group 2")
else:
    print("Group 1")