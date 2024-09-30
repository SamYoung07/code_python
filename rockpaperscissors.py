import random
money = int(input("initial amount of money: "))
initial = money
win = True
#1 = rock
#2 = paper
# = scissors
while win:
    bot = random.randint(1,3)
    player = input("Your move: ")
    if (player == "stop"):
        break
    elif (player == "rock"):
        if (bot == 1):
            print ("Bot Move: rock")
            print ("tie!")
            print(f'Money: ${money}')
        elif (bot == 2):
            print("Bot Move: paper")
            print("You lose!")
            money = 0
            print("Money: $0")
            win = False
        else:
            print("Bot move: scissors")
            print("You win!")
            money = money*2
            print(f"Money: ${money}")
    elif (player == "paper"):
        if (bot == 2):
            print ("Bot Move: paper")
            print ("tie!")
            print(f'Money: ${money}')
        elif (bot == 3):
            print("Bot Move: scissors")
            print("You lose!")
            money = 0
            print("Money: $0")
            win = False
        else:
            print("Bot move: rock")
            print("You win!")
            money = money*2
            print(f"Money: ${money}")
    else:
        if (bot == 3):
            print ("Bot Move: scissors")
            print ("tie!")
            print(f'Money: ${money}')
        elif (bot == 1):
            print("Bot Move: rock")
            print("You lose!")
            money = 0
            print("Money: $0")
            win = False
        else:
            print("Bot move: paper")
            print("You win!")
            money = money*2
            print(f"Money: ${money}")
if (win):
    print(f"Congratulations!")
    print(f"You earned ${money - initial}")