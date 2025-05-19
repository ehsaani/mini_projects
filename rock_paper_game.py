import random, time

options = ("rock", "paper", "scissors")
usser_score = 0
computer_score = 0

while True:
    player = input("Choose between (rock, paper, scissors) or type 'break' to quit: ").lower()
    
    if player == "break":
        print("Game ended.")
        break

    if player not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    
    print("---------------")
    print(f"Player chose {player}")
    print(f"Computer chose {computer}")
    print("---------------")
    time.sleep(3)
    
    if player == computer:
        print("It's a tie.")
    elif (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper") or \
         (player == "rock" and computer == "scissors"):
        print("You win!")
        usser_score += 1
    else:
        print("Computer wins.")
        computer_score += 1
    print("---------------")
    time.sleep(2)
    print(f"Usser Score is: {usser_score}")
    print(f"Computer Score is: {computer_score}")
    print("---------------")
    time.sleep(2)

