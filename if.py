import random
name = input("Enter your name: ")
game = input("Enter your choice (rock, paper, scissors): ")
choice = ["rock", "paper", "scissors"]
computer = random.choice(choice)
print(f"Computer chose: {computer}")
if game == "rock" and computer == "rock":
    print("It's a tie!")
if game == "rock" and computer == "scissors":
        print(f"{name} wins! Rock beats scissors.")

elif game == "rock" and computer == "paper":
        print(f"{name} lost! Paper beats rock.")

# paper
if game == "paper" and computer == "paper":
    print("It's a tie!")

if game == "paper" and computer == "scissors":
        print(f"{name} lost! Scissors beats paper.")

elif game == "paper" and computer == "rock":
        print(f"{name} wins! Rock beats paper.")

# scissors
if game == "scissors" and computer == "scissors":
    print("It's a tie!")

if game == "scissors" and computer == "paper":
        print(f"{name} wins! Scissors beats paper.")

elif game == "scissors" and computer == "rock":
        print(f"{name} lost! Rock beats scissors.")

    