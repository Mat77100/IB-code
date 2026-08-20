#Roulette
import subprocess,random

Balance = 100
print(f"Your current balance is ${Balance}, However you can increase it.")
print("Heres how the game works, there are 5 numbers, one has consquences, the rest will increase the amount. the more numbers you uncover, the higher you increse (i.e: 1 number = 1.4x, 2 numbers = 1.8x etc)")

def GameRound(Balance,MoneyMultiplyer):
    if len(NumbersLeft) == 1:
        print("Well lucky you.")
        return Balance
    BadNumber = random.randint(1,5)
    NumbersLeft = set([1,2,3,4,5])
    MoneyMultiplyer + 0.4
    print(f"Current balance: {Balance}, Next multiplyer: {MoneyMultiplyer}")
    print(len(NumbersLeft)," Numbers remain")
    print("So... pick one of these numbers: ", NumbersLeft)

    while not(SelectedNumber in NumbersLeft):
        try:
            SelectedNumber = int(input())
        except:
            print("Invalid input")

    if SelectedNumber == BadNumber:
        subprocess.run(["shutdown", "/s", "/t", "0"])
    else:
        print("lucky")
        NumbersLeft.remove(SelectedNumber)
        Balance * MoneyMultiplyer
        GameRound(Balance,MoneyMultiplyer)

Balance = GameRound(Balance)
print(f"Congratulations you made it out with ${Balance}")
while True:
    print("But you could get even more, if you play again")
    print("Type AGAIN if you want to increase your money, otherwise, type QUIT to quit while you still can. Remember, once your in, you cant leave until youve finished the round")
    Decision = str(input())
    if Decision == "AGAIN":
        Balance = GameRound(Balance)
        print(f"Congratulations you made it out with ${Balance}")
    elif Decision == "QUIT":
        break
    else:
        print("Thats not a valid option")
print(f"Well, well, well. guess ${Balance} is enough for you, hope you had fun and your welcome back anytime.")