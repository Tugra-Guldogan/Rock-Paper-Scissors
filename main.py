import random

print("-----------WELCOME TO ROCK PAPER SCISSORS SIMULATOR-------------")
print("")
print("Enter any of the following numbers to play the game : ")
print("1 - rock")
print("2 - paper")
print("3 - scissors")
print("")
num = int(input("ENTER YOUR CHOICE : "))
rand = random.randint(1,3)
if rand ==1:
    print("The AI chooses rock")

if rand ==2:
    print("The AI chooses paper")

if rand ==1:
    print("The AI chooses rock")

if num == 1 and rand == 2:
    print("Paper beats rock")
    print("You lose !!")

elif num == 1 and rand == 3:
    print("Rock beats Scissors")
    print("You win !!")

elif num == rand:
    print("Same thing, LOL !!!")

elif num == 2 and rand == 1:
    print("Paper beats rock")
    print("You win !!")

elif num == 2 and rand == 3:
    print("Scissors beats paper")
    print("You lose !!")

elif num == 3 and rand == 1:
    print("Rock beats scissors")
    print("You lose !!")

elif num == 3 and rand == 2:
    print("Scissors beats paper")
    print("You win!!")
