# SIMPLE ROCK PAPER SCISSORS GAME
import random
import time
import os

def anYujin():
    rps = ["Rock", "Paper", "Scissors"]
    An_Yujin_Pick = random.choice(rps)
    return An_Yujin_Pick

def playAgain():
    tieResult = input("it's a Tie! Would you like to play again? (Y/N): ")
    if tieResult == "Y":
        os.system('cls')
        game()
    else:
        os.system('cls')
        print("Thank you for playing this game! :D")
        return
    
    realRes = input("Would you like to play again? (Y/N): ")
    if realRes == "Y":
        os.system('cls')
        game()
    else:
        os.system('cls')
        print("Thank you for playing this game! :D")

def game():
    print("Hi Welcome to The Rock Paper Scissors Game!")
    playerChoice = input("Enter your move (Rock/Paper/Scissors): ")

    print(f"You chose {playerChoice}!")
    print("An Yujin is thinking...")
    time.sleep(2)

    anyujinPick = anYujin()
    print(f"An Yujin picked {anyujinPick}")

    if anyujinPick == "Rock" and playerChoice == "Scissors":
        print("An Yujin Wins!")
    elif anyujinPick == "Scissors" and playerChoice == "Rock":
        print("You Win!")
    elif anyujinPick == "Paper" and playerChoice == "Scissors":
        print("You Win!")
    elif anyujinPick == "Scissors" and playerChoice == "Paper":
        print("An Yujin Wins!")
    elif anyujinPick == "Paper" and playerChoice == "Rock":
        print("An Yujin Wins!")
    elif anyujinPick == "Rock" and playerChoice == "Paper":
        print("You win!")
    else:
        playAgain()

game()