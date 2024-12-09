# Elias Wilber 
# 12/08/2024
# CIS 129
# 12937



import random as r

n = r.randrange(1, 1001)

def game():
    while True:
        print()
        oneGuess = int(input("What is your first guess of the number between 1-1000?\nPlease enter here: "))
        if oneGuess > n:
            print()
            print(f"Your number, {oneGuess}, was too high! Try again.")
            continue
        elif oneGuess < n:
            print()
            print(f"Your nubmber, {oneGuess}, was too small. Try again!")
            continue
        elif oneGuess == n:
            print()
            print(f"Nice! {oneGuess} was correct!")
            break

game()

while True:
    print()
    yOrN = input("Would you like to play the game again? (Y/N): ")
    print()
    yOrN = yOrN.capitalize()
    if yOrN.isalpha() == True:
        break
    else:
        print("You have to enter a alphabetical character (Y/N). Try Again!")
        continue



def check():
    if yOrN == 'Y':
        game()
    else:
        print("Have a good day then.")

check()