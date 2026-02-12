import random

print("Welcome to Rock Paper Scissors!")
print("You will play against the computer. The first to reach 5 wins is the champion!")
print("Enter your choice: rock, paper, or scissors")
playerscore = 0 
computerscore = 0
while playerscore < 5 and computerscore < 5:
    playerchoice = input("Your choice: ")
    computerchoice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer's choice: {computerchoice}")
    if playerchoice == computerchoice:
        print("It's a tie!")
    elif (playerchoice == "rock" and computerchoice == "scissors") or \
         (playerchoice == "paper" and computerchoice == "rock") or \
         (playerchoice == "scissors" and computerchoice == "paper"):
        print("You win!")
        playerscore += 1
    else:
        print("Computer wins!")
        computerscore += 1
    print(f"Score: You {playerscore} - Computer {computerscore}")

if playerscore == 5:
    print("Congratulations! You are the champion!")
elif computerscore == 5:
    print("Computer is the champion! Better luck next time!")

