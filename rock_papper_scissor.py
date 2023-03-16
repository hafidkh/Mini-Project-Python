import random

choices = ["rock", "paper", "scissors"]

print("Rock, Paper, Scissors Let's play!")
player = input("Enter your choice: ")
cpu = random.choice(choices)

print(f"CPU: {cpu}")

if player == cpu:
    print("It's a tie!")
elif (player == "rock" and cpu == "scissors") or (player == "paper" and cpu == "rock") or (player == "scissors" and cpu == "paper"):
    print("You win!")
else:
    print("You lose!")
