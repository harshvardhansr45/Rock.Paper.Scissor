import random

while True:
    user = input("Enter your choice (Rock, Paper, Scissors) or 'q' to quit: ").strip().lower()
    
    if user == 'q':
        print("Thanks for playing! Goodbye! 👋")
        break  
    
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Please enter Rock, Paper, or Scissors.")
        continue  

    computer = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

    print("\n")  
