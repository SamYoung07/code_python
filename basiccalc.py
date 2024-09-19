print("Enter a simple calculation")
print("Seperate numbers and symbols with a space (e.g. 3 x 4)")
x = input()
calc = x.split()
if (calc[1] == "+"):
    print(int(calc[0]) + int(calc[2]))
elif (calc[1] == "-"):
    print(int(calc[0]) - int(calc[2]))
elif (calc[1] == "x"):
    print(int(calc[0]) * int(calc[2]))
elif (calc[1] == "/"):
    print(int(calc[0]) / int(calc[2]))
else: 
    print("invalid input")
